from mypyc.build import mypycify


def build(kwargs):
    kwargs["ext_modules"] = mypycify([
        "live_coverage/live_coverage.py"
    ])
