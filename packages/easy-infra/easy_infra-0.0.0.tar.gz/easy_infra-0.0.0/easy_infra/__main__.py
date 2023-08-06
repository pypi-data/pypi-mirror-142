import logging

from ensurepip import bootstrap
from .commands.bootstrap import init
from .version import __version__
from signal import signal, SIGINT
from sys import exit

from pbr.packaging import get_version

import click

_tool_name = "easy_infra"

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logging.basicConfig(
    format="[%(asctime)s] "
    + _tool_name
    + " [%(levelname)s] %(funcName)s %(lineno)d: %(message)s"
)


def sigint_handler(signal_received, frame):
    """Handle SIGINT or CTRL-C and exit gracefully"""
    logger.warning("SIGINT or CTRL-C detected. Exiting gracefully")
    exit(0)


@click.group(help="CLI tool quickly bootstrap AWS ECS Services")
@click.help_option("--help", "-h")
@click.version_option(
    prog_name=_tool_name, version=get_version(__package__), message="%(prog)s, version %(version)s"
)
def main():
    pass


main.add_command(init)

if __name__ == "__main__":
    signal(SIGINT, sigint_handler)
    main(bootstrap)
