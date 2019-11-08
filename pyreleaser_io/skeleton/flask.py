import pyreleaser_io.skeleton.simple
import pyreleaser_io.util
import pyreleaser_io.template
from halo import Halo
import logging
import os

logger = logging.getLogger(__name__)
description = """
    Bare-bones flask support
    """


def init(project):
    logger.debug("Creating a flask project...")
    project_name = project.get("name")
    project["install_requires"] = ["Flask"]

    pyreleaser_io.skeleton.simple.init(project)

    with Halo(text='Installing flask and wsgi...', spinner='dots'):
        pyreleaser_io.util.run("pipenv install flask uwsgi")
    logger.info("✔️ flask and wsgi installed")

    project_dirs = [
        os.path.join(project_name, "static"),
        os.path.join(project_name, "templates"),
    ]

    project_files = {
        "flask/__init__.py.jinja2": os.path.join(project_name, "__init__.py"),
        "flask/views.py.jinja2": os.path.join(project_name, "views.py"),
        "flask/DEVELOP.md.jinja2": os.path.join("DEVELOP.md"),
        "flask/conftest.py.jinja2": os.path.join("tests", "conftest.py"),
        "flask/test_app.py.jinja2": os.path.join("tests", "test_app.py"),
    }

    for project_dir in project_dirs:
        os.mkdir(project_dir)

    for template_file, target_file in project_files.items():
        pyreleaser_io.template.render_to_file(template_file, target_file, project=project)


    # # views.py - adapted from https://flask.palletsprojects.com/en/1.1.x/patterns/packages/#larger-applications
    # shutil.copy(pyreleaser_io.util.get_res_filename("res/static/flask/views.py"), project_name)
