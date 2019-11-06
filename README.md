# pyreleaser_io

## Status
**This project does _almost_ nothing**

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
| ...CLI executable ready for pypi    | no     |
| ...Flask                            | no     |
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
| autoinstall dependencies            | no     |
| create project with no vcs          | yes    |

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
pip3 install pyreleaser_io --user
pip3 install pipenv --user
pip3 install pyyaml --user
pip3 install jinja2 --user
pip3 install pygithub --user
```

todo: automatic dependency installation

**Creating a project...**

