import argparse

from flask import Flask
from flask_restful import Api

import handlers


def get_args():
    parser = argparse.ArgumentParser(
        prog="python run main.py"
    )
    parser.add_argument("-d", "--debug", type=bool, default=False,
                        help="Debug mode")
    args = parser.parse_args()
    return args


def main():
    command_option_list = get_args()
    app = Flask(__name__)
    api = Api(app)
    handlers.setup(api)
    app.run(debug=command_option_list.debug)
    return


if __name__ == '__main__':
    main()
