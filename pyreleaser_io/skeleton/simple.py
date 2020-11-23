import sys
import os
import pyreleaser_io.template
import pyreleaser_io.util
from halo import Halo
from loguru import logger

description = """
    A simple pipenv project
    """

layout = [
    "MANIFEST.in.jinja2",
    "README.md.jinja2",
    "setup.py.jinja2",
    "Makefile.jinja2"
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
    python_version = f"{sys.version_info[0]}.{sys.version_info[1]}"
    with Halo(text='Creating pipenv...', spinner='dots'):
        status = pyreleaser_io.util.run(f"pipenv install --python {python_version} -e .", False)
        status &= pyreleaser_io.util.run(f"pipenv install --python {python_version} --dev pytest", False)

        if status:
            logger.info("✔️ pipenv created")
