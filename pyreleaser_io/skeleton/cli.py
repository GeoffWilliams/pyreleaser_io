import pyreleaser_io.skeleton.simple
import pyreleaser_io.util
import pyreleaser_io.template
from halo import Halo
import logging
import os

logger = logging.getLogger(__name__)
description = """
    A basic CLI app, ready to publish to pypi
    """


def init(project):
    logger.debug("Creating a cli project...")
    project_name = project.get("name")
    project["console_scripts"] = [f"{project_name}={project_name}.cli:main"],

    pyreleaser_io.skeleton.simple.init(project)

    project_files = {
        "cli/cli.py.jinja2": os.path.join(project_name, "cli.py"),
        "cli/DEVELOP.md.jinja2": os.path.join("DEVELOP.md"),
        "cli/conftest.py.jinja2": os.path.join("tests", "conftest.py"),
        "cli/test_cli.py.jinja2": os.path.join("tests", "test_cli.py"),
    }

    for template_file, target_file in project_files.items():
        pyreleaser_io.template.render_to_file(template_file, target_file, project=project)
