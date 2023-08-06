import hashlib
import io
import runpy
import shutil
import sys
import time
import webbrowser
from argparse import ArgumentParser
from http.server import SimpleHTTPRequestHandler
from multiprocessing import Process, Lock
from pathlib import Path
from socketserver import TCPServer
from threading import Thread
from typing import Any, BinaryIO

from coverage import Coverage
from coverage.exceptions import NoDataError

request_lock = Lock()


class RequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, directory="htmlcov", **kwargs)  # type: ignore

    def send_head(self) -> io.BytesIO | BinaryIO | None:
        with request_lock:
            return super().send_head()

    def log_message(self, *_: Any) -> None:
        pass


def start_server() -> Process:
    def start() -> None:
        with TCPServer(("127.0.0.1", 0), RequestHandler) as httpd:
            port = httpd.socket.getsockname()[1]
            webbrowser.open(f"http://localhost:{port}/")
            httpd.serve_forever()

    process = Process(target=start)
    process.start()
    return process


def update_script(data_hash: str) -> None:
    file = Path("htmlcov/coverage_html.js")
    content = file.read_text()
    content = f"""const HASH = "{data_hash}";\n\n""" + content
    content += """
    const interval = setInterval(() => {
        fetch(location.origin + "/coverage_html.js").then(r => r.text()).then(r => {
            const new_hash = r.split('"')[1];
            if (new_hash !== HASH) location.reload();
        }).catch(() => clearInterval(interval));
    }, 1000);
    """
    file.write_text(content)


def main() -> None:
    def get_file(p: str) -> Path:
        out = Path(p)
        if not out.is_file():
            raise ValueError
        return out

    parser = ArgumentParser()
    parser.add_argument("-a", "--append", action="store_true", help="Append coverage data instead of starting clean")
    parser.add_argument("-b", "--branch", action="store_true", help="Measure branch coverage")
    parser.add_argument("-c", "--clean", action="store_true", help="Remove htmlcov/")
    parser.add_argument("-s", "--save", action="store_true", help="Save data to .coverage")
    parser.add_argument("-t", "--timid", action="store_true", help="Use simpler trace method")
    parser.add_argument("file", type=get_file, help="Python program file")
    args = parser.parse_args()

    sys.path.insert(0, str(args.file.parent.absolute()))

    cov = Coverage(auto_data=args.append, timid=args.timid, branch=args.branch, omit=[__file__])

    def update_coverage() -> None:
        time.sleep(1)
        last: float = 0
        last_data_hash = ""
        while True:
            now = time.time()
            time.sleep(max(last + 1 - now, 0))
            last = now
            if not cov._started:  # noqa
                break

            data_hash = hashlib.sha256(cov.get_data().dumps()).hexdigest()
            if data_hash == last_data_hash:
                continue

            with request_lock:
                try:
                    cov.html_report()
                except NoDataError:
                    pass
                else:
                    update_script(data_hash)
                    last_data_hash = data_hash

    path = Path("htmlcov/index.html")
    if not path.exists():
        path.parent.mkdir(exist_ok=True)
        path.write_text("""<html><head><meta http-equiv="refresh" content="1"></head><body></body></html>""")

    cov.start()
    thread = Thread(target=update_coverage)
    thread.start()

    server = start_server()

    try:
        runpy.run_path(str(args.file), {}, "__main__")
    finally:
        cov.stop()
        thread.join()

        if args.save:
            cov.save()

        cov.report()

        server.kill()

        if args.clean:
            shutil.rmtree("htmlcov")
        else:
            cov.html_report()
            webbrowser.open("htmlcov/index.html")
