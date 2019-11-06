import pyreleaser_io.create
import tempfile
import os


def test_create():
    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    project = {
        "name": "test_proj"
    }

    pyreleaser_io.create.create_project(project)

    assert os.path.isdir("test_proj")
    assert os.path.isdir("test_proj/test_proj")
    assert os.path.isfile("test_proj/test_proj/__init__.py")
    assert os.path.isfile("test_proj/README.md")
    assert os.path.isfile("test_proj/setup.py")
    assert os.path.isfile("test_proj/MANIFEST.in")