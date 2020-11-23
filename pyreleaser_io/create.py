import logging
import pyreleaser_io.vcs.github
import pyreleaser_io.vcs.missing
import pyreleaser_io.util
import pyreleaser_io.skeleton
import os
import pkgutil
import importlib
from consolemenu import *
from consolemenu.items import *

logger = logging.getLogger(__name__)


vcs = {
    "github": pyreleaser_io.vcs.github,
    "none": pyreleaser_io.vcs.missing
}

def get_skeletons():
    skeletons = {}
    # fixme... can this all be done with importlib?
    for importer, modname, ispkg in pkgutil.iter_modules(pyreleaser_io.skeleton.__path__):
        skeletons[modname] = importlib.import_module("." + modname, package="pyreleaser_io.skeleton")
        #print("Found submodule %s (is a package: %s)" % (modname, ispkg))
    return skeletons


def get_vcs(settings):
    driver = False
    _module = None
    for name, module in vcs.items():
        logger.debug(f"trying to setup VCS {name}")
        _module = module
        driver = module.get_instance(settings.get(name, {}))
        if driver:
            logger.debug(f"got a VCS driver! {name}")
            break

    return _module, driver


def interactive(settings, online):
    print("Lets make something...")
    project = {"name": input("project name? ")}

    default_description = "I'll add this later..."

    project["description"] = input(f"Project description? [{default_description}]") or default_description

    if project["description"] == default_description:
        logger.info("sure you will")

    skeletons = get_skeletons()
    skeleton_items = list(skeletons.keys())
    selection_menu = SelectionMenu(skeleton_items, title="choose skeleton", show_exit_option=False)
    selection_menu.show()
    selection_menu.join()
    project["skeleton"] = skeletons.get(skeleton_items[selection_menu.selected_option])

    if online:
        vcs_module, vcs_driver = get_vcs(settings)
        default_project_url = vcs_module.project_url(project, vcs_driver)
        project["url"] = input(f"Project URL? [{default_project_url}]") or default_project_url
        vcs_module.add_user_info(project, vcs_driver)

    create_project(project)

    print("all done!")


def create_project(project):
    project_name = project.get("name")
    if os.path.isdir(project_name):
        raise RuntimeError(f"Already exists: {project_name}")

    logger.info("Creating skeleton...")
    os.mkdir(project_name)
    pwd = os.getcwd()
    os.chdir(project_name)

    project["skeleton"].init(project)

    os.chdir(pwd)
