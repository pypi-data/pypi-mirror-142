import hashlib
import runpy
import sys
import time
import webbrowser
from argparse import ArgumentParser
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from socketserver import TCPServer
from threading import Thread
from multiprocessing import Process
from typing import Any

from coverage import Coverage


class RequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, directory="htmlcov", **kwargs)  # type: ignore

    def log_message(self, *_: Any) -> None:
        pass


def start_server() -> Process:
    def start() -> None:
        time.sleep(1)
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
    setInterval(() => {
        fetch(location.origin + "/coverage_html.js").then(r => r.text()).then(r => {
            const new_hash = r.split('"')[1];
            if (new_hash !== HASH) location.reload();
        });
    }, 1000);
    """
    file.write_text(content)


def main() -> None:
    def get_file(path: str) -> Path:
        out = Path(path)
        if not out.is_file():
            raise ValueError
        return out

    parser = ArgumentParser()
    parser.add_argument("-a", "--append", action="store_true", help="Append coverage data instead of starting clean")
    parser.add_argument("--branch", action="store_true", help="Measure branch coverage")
    parser.add_argument("--timid", action="store_true", help="Use simpler trace method")
    parser.add_argument("file", type=get_file, help="Python program file")
    args = parser.parse_args()

    sys.path.insert(0, str(args.file.parent.absolute()))

    cov = Coverage(auto_data=args.append, timid=args.timid, branch=args.branch, omit=[__file__])

    def update_coverage() -> None:
        while cov._started:  # noqa
            time.sleep(1)
            cov.save()
            cov.html_report()
            update_script(hashlib.sha256(cov.get_data().dumps()).hexdigest())

    cov.start()
    thread = Thread(target=update_coverage)
    thread.start()

    server = start_server()

    try:
        runpy.run_path(str(args.file), {}, "__main__")
    finally:
        cov.stop()
        thread.join()

        cov.save()
        cov.html_report()
        cov.report()

        webbrowser.open("htmlcov/index.html")

        time.sleep(3)

        server.kill()
