"""
Module Description.


"""
import json
import logging
import os
from pathlib import Path

CWD = Path.cwd()
logger = logging.getLogger(__name__)


def initialise(projectname: str, no_init: bool, no_install: bool) -> None:
    PROJDIR = CWD.absolute() / projectname
    # Change to project DIR
    os.chdir(PROJDIR)

    vscode_settings = {
        "python.formatting.provider": "yapf",
        "python.linting.flake8Enabled": True,
        "files.autoSave": "afterDelay",
        "python.testing.pytestArgs": ["test"],
        "python.testing.unittestEnabled": False,
        "python.testing.pytestEnabled": True
    }
    VSDIR = PROJDIR / '.vscode'
    VSDIR.mkdir(exist_ok=True, parents=True)
    with open(VSDIR / 'settings.json', 'w') as f:
        json.dump(vscode_settings, f)

    if not no_install:
        os.system('pipenv install -d')

    # Init GIT
    if not no_init:
        git_init = ['git init', 'git add -A', 'git commit -m "first commit"']
        for cmd in git_init:
            os.system(cmd)
