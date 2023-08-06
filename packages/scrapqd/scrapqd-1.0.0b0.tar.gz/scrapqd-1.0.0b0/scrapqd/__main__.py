import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="ip address to run the ScrapQD server", default="127.0.0.1")
parser.add_argument("--port", help="port to run the ScrapQD server", type=int, default=5000)
parser.add_argument("--debug", help="run server in debug mode", action="store_true", default=False)
args = parser.parse_args()


def add_project_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, current_dir)


def run():
    from scrapqd.app import run as standalone_run  # noqa
    standalone_run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    add_project_path()
    run()
