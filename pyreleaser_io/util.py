from loguru import logger
import sys
import pathlib
import os
import yaml
import subprocess




def setup_logging(level, logger_name=None):
    logger_name = logger_name or __name__.split(".")[0]
    log_formats = {
        "DEBUG": "{time} {level} {message}",
        "INFO": "{message}",
    }

    logger.remove()
    logger.add(sys.stdout, format=log_formats[level], filter=logger_name, level=level)
    logger.debug("====[debug mode enabled]====")


def settings():
    settings_file = os.path.join(str(pathlib.Path.home()), ".pyreleaser_io.yaml")
    if os.path.isfile(settings_file):
        logger.debug("parsing: %s", settings_file)
        with open(settings_file, 'r') as f:
            data = yaml.safe_load(f.read())
    else:
        logger.warning(f"skipping missing settings file: {settings_file}")
        data = {}

    return data.get("pyreleaser_io", {})


def run(cmd, check=True):
    """
    run a command, return true if it worked otherwise false
    cmd - command to run (array)

    """
    status = False
    try:
        # RHEL8 uses python 3.6 so we're stuck with `check_output()` for the next
        # few years
        logger.debug(f"running command {cmd} in directory {os.getcwd()}")
        _ = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode().strip()
        status = True
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
        if check:
            logger.error(output)
            raise e
        else:
            logger.warning(output)

    return status


def get_res_filename(filename):
    return os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        filename
    )


def get_res_file_content(filename):
    with open(get_res_filename(filename), "r") as f:
        return f.read()
