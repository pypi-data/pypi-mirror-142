import os
import shutil
import stat
from pathlib import Path
from typing import Dict
from urllib.parse import urlparse

import coloring

from . import consts
from .bases import fw_toolsmanager, pm_tasks
from .exceptions import (
    CmdAlreadyExistException,
    CmdDontExistException,
    ToolDontExistsException,
)
from .utils import load_database, run


def normalize_git_repo(repo):
    parsed_url = urlparse(repo)
    if not parsed_url.path:
        raise ValueError("Incorrect URL REPO")

    scheme = parsed_url.scheme or "https"
    site = parsed_url.netloc or "github.com"
    path = parsed_url.path
    if path[0] == "/":
        path = path[1:]
    if path[-1] == "/":
        path = path[:-1]
    owner, directory = path.split("/")
    return {
        "owner": owner,
        "directory": directory,
        "fullurl": f"{scheme}://{site}/{owner}/{directory}",
        "site": site,
    }


def gitclone(repository: str, directory: str = None, verbose=True):
    # TODO: bydefault clone github? Example toolsmanager git clone nazime/toolsmanager
    # TODO: add possibility to clone many repository at once
    parsed_repo = normalize_git_repo(repository)
    if directory is None:
        directory = parsed_repo["directory"]

    cmd = [
        "git",
        "-C",
        consts.TM_GIT,
        "clone",
        parsed_repo["fullurl"],
        directory,
        "--depth",
        "1",
    ]

    results = run(cmd)
    if verbose:
        if b"already exists and is not an empty directory" in results.stderr:
            coloring.print_failure(f"directory {directory!r} already exist")
        else:
            coloring.print_success(f"directory {directory!r} cloned")

    return {"tool_directory": os.path.join(os.path.join(consts.TM_GIT, directory))}


# ======= #
# gitpull #
# ======= #
def gitpull(rootpath: str = None):
    if rootpath is None:
        rootpath = consts.TM_GIT

    nb_uptodate = 0
    nb_updated = 0
    total = 0
    for basedir in os.listdir(rootpath):
        dirpath = os.path.join(rootpath, basedir)
        if not os.path.isdir(dirpath):
            continue

        # check if we can read the dir
        if not os.access(dirpath, os.R_OK):
            continue

        # check if it is a github repo
        if ".git" not in os.listdir(dirpath):
            continue

        coloring.print_info("Git repo found:", dirpath)
        result = run(["git", "-C", dirpath, "pull"])
        if b"Already up to date" in result.stdout:
            coloring.print_info(basedir, "already up to date")
            nb_uptodate += 1
        else:
            coloring.print_success(basedir, "updated")
            nb_updated += 1
        total += 1
    if total:
        print()
        coloring.print_info(f"{nb_uptodate}/{total} already up to date")
        if nb_updated:
            coloring.print_success(f"{nb_updated}/{total} updated")
        else:
            coloring.print_info(f"{nb_updated}/{total} updated")
    else:
        coloring.print_failure("No git repositories founds")


def lsgit():
    git_projects = os.listdir(consts.TM_GIT)
    coloring.print_success(f"found {len(git_projects)} git projects")
    for project in git_projects:
        print(project)


def rmgit(project_name: str):
    project_path = os.path.join(consts.TM_GIT, project_name)
    if not os.path.exists(project_path):
        coloring.print_failure(f"Project {project_name!r} don't exist")
        return
    shutil.rmtree(project_path)
    coloring.print_success(f"Project {project_name!r} removed")


# --- CMD ---
# -----------


def addcmd(cmdpath: str, cmdname: str = None):
    if cmdname is None:
        cmdname = os.path.basename(cmdpath)

    cmdpath = os.path.realpath(cmdpath)

    # chmod u+x on the original file
    st = os.stat(cmdpath)
    os.chmod(cmdpath, st.st_mode | stat.S_IEXEC)

    if cmdname in os.listdir(consts.TM_BIN):
        raise CmdAlreadyExistException(f"command {cmdname!r} already exist")

    # add symlink
    os.symlink(cmdpath, os.path.join(consts.TM_BIN, cmdname))


def rmcmd(cmdname: str):
    cmdpath = os.path.join(consts.TM_BIN, cmdname)
    if not os.path.exists(cmdpath):
        raise CmdDontExistException(f"command {cmdname!r} don't exist")

    os.remove(cmdpath)


# TODO: rm cmd taking many cmd names to remove?


def lscmd() -> Dict[str, str]:
    """Return a dict of all Cmd with their name and symlinkg target"""
    commands = {}
    for cmd in os.listdir(consts.TM_BIN):
        cmd_path = Path(consts.TM_BIN) / Path(cmd)
        if Path(cmd_path).is_symlink():
            symlink = str(Path(cmd_path).resolve())
        else:
            symlink = ""
            # Fixme: Possible to not use symlink? maby after with python scripts
        commands[cmd] = symlink
    return commands


def clearcmd():
    for cmdname in os.listdir(consts.TM_BIN):
        cmdpath = os.path.join(consts.TM_BIN, cmdname)
        os.remove(cmdpath)


# --- VARS ---
# ------------
def addvar(varname: str, varvalue: str):
    fw_toolsmanager.dict_db["vars"][varname] = varvalue


def rmvar(varname: str):
    del fw_toolsmanager.dict_db["vars"][varname]


def lsvar():
    return dict(fw_toolsmanager.dict_db["vars"])


def clearvar():
    fw_toolsmanager.dict_db["vars"].clear()


# ------ INSTALL --------
# -----------------------
def install(*toolnames):
    """Install one or more tools"""
    # load DB

    if isinstance(toolnames, str):
        toolnames = [toolnames]
    tools = load_database()

    for toolname in toolnames:
        try:
            tool = tools[toolname]
        except KeyError:
            raise ToolDontExistsException

        # TODO: Install deps
        # Create metadata to give to all tasks
        meta = {}
        # Keep track of previous_tasks
        previous_tasks = []

        # Instantiate all tasks before, to check if root is required
        tasks = []
        for raw_task in tool["tasks"]:
            raw_task = dict(raw_task)
            Task = pm_tasks[raw_task["task"]]
            kwargs = dict(raw_task)
            kwargs.pop("task")
            task = Task(**kwargs)
            tasks.append(task)

        print(toolname)
        print(f"  tasks:", tasks)
        requires_root = any(e.requires_root() for e in tasks)
        print("  requires_root", requires_root)
        for raw_task in tool["tasks"]:
            raw_task = dict(raw_task)

            Task = pm_tasks[raw_task["task"]]
            kwargs = dict(raw_task)
            kwargs.pop("task")
            task = Task(**kwargs)
            # Update metadata and previous_tasks
            task.meta.update(meta)
            task.previous_tasks = previous_tasks
            if not task.isinstalled():
                print(f"  task {task.name} not installed. Installing")
                task.install()
            else:
                print(f"  task {task.name} installed")
            meta.update(task.get_metadata())
            previous_tasks.append(task)


def isinstalled(toolname):
    # load DB

    tools = load_database()
    try:
        tool = tools[toolname]
    except KeyError:
        raise ToolDontExistsException

    # TODO: Install deps

    for task in tool["tasks"]:
        task = dict(task)

        Task = pm_tasks[task["task"]]
        task.pop("task")
        task = Task(**task)
        print("task", task)
        task.run()
    print("Installing", tool)


def uninstall(toolname):
    # load DB

    tools = load_database()
    try:
        tool = tools[toolname]
    except KeyError:
        raise ToolDontExistsException

    # iter in reversed order
    for task in tool["tasks"][::-1]:
        task = dict(task)
        Task = pm_tasks[task["task"]]
        task.pop("task")
        task = Task(**task)
        print("task", task)
        task.uninstall()
