import os
import pyreleaser_io.template
import pyreleaser_io.util
from halo import Halo
import logging

logger = logging.getLogger(__name__)

description = """
    A simple pipenv project
    """

layout = [
    "MANIFEST.in.jinja2",
    "README.md.jinja2",
    "setup.py.jinja2"
]


def init(project):
    logger.debug("Creating a simple project...")
    project_name = project.get("name")
    project_src = project_name
    project_res = os.path.join(project_src, "res")
    init_py = os.path.join(project_src, "__init__.py")

    for template_file in layout:
        pyreleaser_io.template.render_to_file(
            template_file,
            target_dir=project_name,
            project=project
        )
    os.mkdir(project_src)
    os.mkdir("tests")
    os.mkdir(project_res)
    open(init_py, "a").close()

    with Halo(text='Creating pipenv...', spinner='dots'):
        pyreleaser_io.util.run("pipenv install -e .")
        pyreleaser_io.util.run("pipenv install --dev pytest")
    logger.info("✔️ pipenv created")

