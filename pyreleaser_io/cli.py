"""pyreleaser - python release helper tool

Usage:
  pyreleaser [--debug] [--offline] <command>
  pyreleaser --version

Arguments:
  <command> create-project

Options:
  -h --help     Show this screen.
  --version     Show version.
  --debug       Extra debugging messages
  --offline     work offline

"""
from loguru import logger
from docopt import docopt
import pyreleaser_io.util
import pkg_resources
import pyreleaser_io.create
import pyreleaser_io.util


def version():
    return pkg_resources.require("pyreleaser_io")[0].version


def main():
    arguments = docopt(__doc__, version=pkg_resources.require("pyreleaser_io")[0].version)
    pyreleaser_io.util.setup_logging("DEBUG" if arguments['--debug'] else "INFO")

    settings = pyreleaser_io.util.settings()

    if arguments["<command>"] == "create-project":
        pyreleaser_io.create.interactive(settings, not arguments["--offline"])
    else:
        raise RuntimeError("bad invocation")
