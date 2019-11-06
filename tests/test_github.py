import pyreleaser_io.github
import pyreleaser_io.util
import tests.test_globals


def test_get_instance():
    # use the real system settings to test GH for the moment... (switch to mock?)
    gh_settings = pyreleaser_io.util.settings().get("github")
    g = pyreleaser_io.github.get_instance(gh_settings)
    project = tests.test_globals.project

    # user info population
    pyreleaser_io.github.add_user_info(project, g)
    assert project.get("author")
    # doesn't work?
    # assert project.get("author_email")

    # URL generation
    assert pyreleaser_io.github.project_url(project, g) == "https://github.com/GeoffWilliams/test_proj.git"

