import os
import shlex

import coloring

from . import consts
from .bases import BaseTask
from .consts import IsInstalledStatus
from .functions import addcmd, gitclone, normalize_git_repo, rmcmd, rmgit
from .printer import printer
from .utils import run


class GitTask(BaseTask):
    name = "git"

    def __init__(self, repo):
        super().__init__()
        self.repo = repo
        parsed_repo = normalize_git_repo(repo)
        self.fullurl = parsed_repo["fullurl"]
        self.directory = parsed_repo["directory"]

    def _cmd_install(self):
        cmd = [
            "git",
            "-C",
            consts.TM_GIT,
            "clone",
            self.fullurl,
            self.directory,
            "--depth",
            "1",
        ]
        return cmd

    def uninstall(self):
        normalized_repo = normalize_git_repo(self.repo)
        directory = normalized_repo["directory"]
        coloring.print_info(f"Removing git directory {directory}")
        rmgit(directory)

    def install(self):
        coloring.print_info(f"Cloning repository {self.fullurl!r}")
        run(self._cmd_install())

    def isinstalled(self):
        if os.path.exists(os.path.join(consts.TM_GIT, self.directory)):
            return IsInstalledStatus.YES
        # Check if tool is installed in root
        elif os.path.exists(os.path.join(consts.TM_GIT_ROOT, self.directory)):
            return IsInstalledStatus.YES
        else:
            return IsInstalledStatus.NO

    def get_metadata(self):
        if consts.is_root:
            return {
                "tool_directory": os.path.join(
                    os.path.join(consts.TM_GIT_ROOT, self.directory)
                )
            }
        else:
            return {
                "tool_directory": os.path.join(
                    os.path.join(consts.TM_GIT, self.directory)
                )
            }

    def __str__(self):
        return f"{self.__class__.__name__}(repo={self.repo})"

    def howtoinstall(self):
        install_sh = "# git clone\n"
        install_sh += shlex.join(self._cmd_install())
        return install_sh


class AptTask(BaseTask):
    name = "apt"
    _installed = None

    def __init__(self, toolname):
        super().__init__()
        self.toolname = toolname

    def install(self):
        printer.info(f"Task {self.name}", repr(self.howtoinstall()))
        results = run(self._cmd_install())
        if results.returncode == 0:
            return "OK"
        print(results)

    def isinstalled(self):
        if self.__class__._installed is None:
            cmd_return = run(["apt", "list", "--installed"])
            tools = cmd_return.stdout.decode().splitlines()[
                1:
            ]  # remove first one "Listing..."
            tools = [e.split("/")[0] for e in tools]
            self.__class__._installed = set(tools)

        if self.toolname in self._installed:
            return IsInstalledStatus.YES
        else:
            return IsInstalledStatus.NO

    def uninstall(self):
        run(["apt", "remove", self.toolname, "-y"])

    def requires_root(self):
        return True

    def __str__(self):
        return f"{self.__class__.__name__}(toolname={self.toolname})"

    def _cmd_install(self):
        cmd = ["sudo", "apt", "install", self.toolname, "-y"]
        return cmd

    def howtoinstall(self):
        return shlex.join(self._cmd_install())

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class BinTask(BaseTask):
    name = "bin"

    def __init__(self, executables, fromdir=False):
        """fromdir => must cd in directory before"""
        super().__init__()
        if isinstance(executables, str):
            executables = [executables]
        self.executables = executables

    def install(self):
        for executable in self.executables:
            if ":" in executable:
                executable, cmdname = executable.split(":")
            else:
                cmdname = None
            tool_directory = self.meta["tool_directory"]
            cmdpath = f"{tool_directory}/{executable}"
            cmdname_str = cmdname or os.path.basename(executable)
            coloring.print_info(
                f"Adding bin shortcut {executable!r} -> {cmdname_str!r}"
            )
            addcmd(cmdpath, cmdname)

    def isinstalled(self) -> consts.IsInstalledStatus:
        for executable in self.executables:
            if ":" in executable:
                executable = executable.split(":")[1]
            if not os.path.exists(os.path.join(consts.TM_BIN, executable)):
                return consts.IsInstalledStatus.NO
        return consts.IsInstalledStatus.YES

    def uninstall(self):
        for executable in self.executables:
            if ":" in executable:
                executable = executable.split(":")[1]

            coloring.print_info(f"Removing bin shortcut {executable!r}")
            rmcmd(executable)

    def __str__(self):
        return f"BinTask(executables={self.executables!r})"

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class DlTask(BaseTask):
    name = "dl"

    def __init__(self):
        super().__init__()

    def uninstall(self):
        # Do nothing
        pass

    def install(self):
        url_repo = f"https://github.com/{self.repo}"
        x = gitclone(url_repo)
        return x

    def isinstalled(self):
        dir_git = self.repo.split("/")[1]
        return os.path.exists(os.path.join(consts.TM_GIT, dir_git))

    def __str__(self):
        return f"DlTask(repo={self.repo!r})"

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class SnapTask(BaseTask):
    name = "snap"
    _installed = None

    def __init__(self, toolname, classic=False):
        super().__init__()
        self.toolname = toolname
        self.classic = classic

    def requires_root(self):
        return True

    def uninstall(self):
        # Do nothing
        pass

    def _install_cmd(self):
        cmd = ["sudo", "snap", "install", self.toolname]
        if self.classic:
            cmd.append("--classic")
        return cmd

    def _uninstall_cmd(self):
        return ["sudo", "snap", "remove", self.toolname]

    def install(self):
        printer.info("Task", self.name, self.howtoinstall())
        run(self._install_cmd())

    def isinstalled(self):
        if self.__class__._installed is None:
            cmd_return = run(["snap", "list"])
            tools = cmd_return.stdout.decode().splitlines()[
                1:
            ]  # fist  line are headers
            tools = [e.split()[0] for e in tools]
            self.__class__._installed = set(tools)

        if self.toolname in self._installed:
            return IsInstalledStatus.YES
        else:
            return IsInstalledStatus.NO

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.toolname})"


class BashTask(BaseTask):
    name = "bash"

    def __init__(self, path: str, root=False):
        super().__init__()
        self.path = path
        self.root = root

    def requires_root(self):
        return self.root

    def uninstall(self):
        # Do nothing
        pass

    def install(self):
        print("meta in bash", self.meta)
        path = os.path.join(self.meta["tool_directory"], self.path)
        run(path, None, None)

    def isinstalled(self):
        return False

    def __str__(self):
        return f"{self.__class__.__name__}(path={self.path})"

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class MageTask(BaseTask):
    name = "mage"

    def install(self):
        pass

    def isinstalled(self):
        return False

    def __str__(self):
        return f"{self.__class__.__name__}()"


class WwwTask(BaseTask):
    # Copy the file to "www" to be shared after
    name = "www"

    def __init__(self, path):
        super().__init__()

    def install(self):
        pass

    def isinstalled(self):
        return False

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class ShrcTask(BaseTask):
    # add the content file to ".bashrc" ".zshrc", ...
    name = "shrc"

    def __init__(self, content):
        super().__init__()
        self.content = content

    def _iter_shrc_filepath(self):
        for rcfile in [".bashrc", ".zshrc"]:
            rcfile = os.path.join(consts.USERHOME, rcfile)
            if os.path.isfile(rcfile):
                yield rcfile

    def _get_normalized_content(self):
        return "\n" + self.content + "\n"

    def install(self):
        # TODO: add .zshrc
        content = self._get_normalized_content()
        for rcfile in self._iter_shrc_filepath():
            if content not in open(rcfile).read():
                open(rcfile, "a").write(content)

    def isinstalled(self):
        content = self._get_normalized_content()
        for rcfile in self._iter_shrc_filepath():
            if content not in open(rcfile).read():
                return IsInstalledStatus.NO
        return IsInstalledStatus.YES

    def uninstall(self):
        content = self._get_normalized_content()
        for rcfile in self._iter_shrc_filepath():
            rc_content = open(rcfile).read()
            if content in rc_content:
                rc_content = rc_content.replace(content, "")
                open(rcfile).write(rc_content)

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def is_tasktool_installed(self):
        return IsInstalledStatus.YES


class GoTask(BaseTask):
    # add the content file to ".bashrc" ".zshrc", ...
    name = "go"

    def __init__(self, args):
        super().__init__()
        self.args = args

    def install(self):
        # TODO: add .zshrc
        run("go", *self.args)

    def __str__(self):
        return f"{self.__class__.__name__}()"
