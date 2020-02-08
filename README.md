# pyreleaser_io

## Status
**Very experimental** 😎

## Overview
This project is a response to a twitter post over at: 
https://twitter.com/garethr/status/1190968258712809472

Aim is to make creating, testing, publishing python projects a bit easier!

# Current development focus
* Creating projects

# What's working so far?

| Task                                | Status |
| ---                                 | ---    |
| Create a new project (GH)           | no     |
| Create a new project (files)        | yes    |
| ...plain/pipenv ready for pypi      | yes    |
| ...CLI executable ready for pypi    | yes    |
| ...Flask                            | yes    |
| ...Docker (for generated projects)  | no     |
| ...setup.py wizard                  | no     |
| Testing/CI setup                    | no     |
| wheel building                      | no     |                        
| wheel uploading                     | no     |
| secure credential storage (keyring) | no     |
| support for bitbucket cloud         | no     |
| support for bitbucket server        | no     |
| support for gitlab                  | no     |
| support for travis                  | no     |
| support for circleci                | no     |
| *AAS for use by other systems       | no     |
| programatic settings file creation  | no     |
| autoinstall dependencies            | yes    |
| create project with no vcs          | yes    |
| pyinstaller support                 | no     |
| Makefile support                    | no     |
| user-customisable templates         | no     |
| logger for flask                    | no     |


# settings file format?

```yaml
---
pyreleaser_io:
  github:
    token: yourgithubtoken
```


# Quickstart

**Install pyreleaser**

```shell
sudo yum install python3
pip3 install pygithub --user
```


**Creating a project...**

## Tips and tricks

**Including non-python files in your wheel**
Including non-python files requires a bit of work so we do it all for you...

Integration points:
* `/setup.py` in `setuptools.setup()`: `include_package_data=True`
* `/MANIFEST.in` - file patterns to include
* `/yourpakage/res` - folder of files to include

Reference: https://packaging.python.org/guides/using-manifest-in/

**getting the filename of bundled files**
```python
    os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        filename
    )
```



## Troublshooting
creating projects always fails with error:

```
pipenv.vendor.requirementslib.exceptions.RequirementError: Error parsing requirement . -- are you sure it is installable?
```

I run `pipenv` manually and get the same error - nothing fixes this, what
gives?

This can be caused by an errant `Pipfile` _above_ the directory you are
working in. Try moving it out of the way

## Developing

**Run tests with coverage**

(once) pipenv install --dev
make test