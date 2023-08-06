import logging

import click
import click_log

from click_default_group import DefaultGroup

from .utils import (
    die,
    file_exists,
    find_key_in_data,
    find_terraform_files,
    process_yaml,
    replace_in_text_file,
)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.help_option("--help", "-h")
@click.group(cls=DefaultGroup, default="list", default_if_no_args=True)
def init():
    """Commands to bootstrap AWS ECS Services"""
    pass


@init.command(context_settings=CONTEXT_SETTINGS)
@click.option("--profile", default=None, help="aws profile")
@click.option("--today", is_flag=True, help="list cluster inits created today")
@click_log.simple_verbosity_option(
    logger,
    default="ERROR",
    help="Either CRITICAL, ERROR, WARNING, INFO or DEBUG, default is ERROR",
)
def list(profile, today):
    """List location of config file"""
    # here = current_directory_path()
    # print(f"Here: {here}")

    # first try default location: easy.yml
    if file_exists("easy.yml"):
        print("Found easy.yml")

        # try read yml file
        processed_yaml = process_yaml("easy.yml")
        # print(json.dumps(processed_yaml, indent=4))

        keys = [
            'name',
            'environments',
            'production',
            'staging',
            'service_count_min',
        ]

        values = {}

        for key in keys:
            try:
                values[key] = find_key_in_data(processed_yaml, key)
                print(f"Found {key}: {values[key]}")
            except KeyError:
                die(f"Could not find {key}")

        # find all terraform files
        files = find_terraform_files()
        for file in files:
            # print(f"Found terraform file: {file}")
            replace_in_text_file(
                file, "%%REPLICA_MIN_COUNT_REPLACE%%", f"{values['service_count_min']}"
            )
