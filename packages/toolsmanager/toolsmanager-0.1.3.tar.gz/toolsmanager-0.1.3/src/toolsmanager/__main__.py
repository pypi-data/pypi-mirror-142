import os

import coloring
import toolsmanager
from koalak import ArgparseSubcmdHelper
from toolsmanager import consts, fw_toolsmanager, get_current_toolsmanager
from toolsmanager.exceptions import CmdAlreadyExistException, CmdDontExistException


class VarCommand(ArgparseSubcmdHelper):
    # add
    description_add = "Add a persistent env variable"

    def parser_add(self, parser):
        parser.add_argument("varname")
        parser.add_argument("varvalue")

    def run_add(self, args):
        toolsmanager.addvar(args.varname, args.varvalue)
        coloring.print_success(f"Variable {args.varname!r} added")
        print(f"run the following line to have the changes in current shell")
        print(f". {fw_toolsmanager.substitute_string('$vars_path')}")

    # rm
    def parser_rm(self, parser):
        parser.add_argument("varname", help="Name of the variable to remove")

    description_rm = "Remove a persistent env variable added with toolsmanager"

    def run_rm(self, args):
        try:
            toolsmanager.rmvar(args.varname)
            coloring.print_success(f"variable {args.varname!r} removed")
        except KeyError:
            coloring.print_failure(f"variable {args.varname!r} don't exist")

    # ls
    description_ls = "List all env variables added with toolsmanager"

    def run_ls(self, args):
        vars = toolsmanager.lsvar()
        if len(vars) == 0:
            coloring.print_info("No variables found")
        else:
            for k, v in vars.items():
                print(f"{k}={v}")

    # clear
    description_clear = "Remove all env variables added with toolsmanager"

    def run_clear(self, args):
        toolsmanager.clearvar()
        coloring.print_success(f"Env variables cleared")


class CmdCommand(ArgparseSubcmdHelper):
    # ====== #
    # addcmd #
    # ====== #
    description_add = "Add a command"

    def parser_add(self, parser):
        parser.add_argument("cmdpath", help="Folder containing git projects")
        parser.add_argument("cmdname", help="Folder containing git projects", nargs="?")

    def run_add(self, args):
        try:
            toolsmanager.addcmd(args.cmdpath, args.cmdname)
            coloring.print_success(f"command {args.cmdname!r} added")
        except CmdAlreadyExistException:
            cmdname = os.path.basename(args.cmdpath)
            coloring.print_failure(f"command {cmdname!r} already exist")

    # ===== #
    # rmcmd #
    # ===== #
    description_rm = "Remove a command"

    def parser_rm(self, parser):
        parser.add_argument("cmdname", help="Folder containing git projects")

    def run_rm(self, args):
        try:
            toolsmanager.rmcmd(args.cmdname)
            coloring.print_success(f"command {args.cmdname} removed")
        except CmdDontExistException:
            coloring.print_failure(f"command {args.cmdname} don't exist")

    description_ls = "List all commands added with toolsmanager"

    def run_ls(self, args):
        commands = toolsmanager.lscmd()
        coloring.print_success(f"found {len(commands)} commands")
        for cmd, symlink in commands.items():
            print(f"{cmd} {coloring.green('->')} {symlink}")

    # clear
    description_clear = "Remove all commands added with toolsmanager"

    def run_clear(self, args):
        toolsmanager.clearcmd()
        coloring.print_success(f"Commands cleared")


class GitCommand(ArgparseSubcmdHelper):
    # ======== #
    # gitclone #
    # ======== #
    description_gitclone = "Clone repository to toolsmanager GIT folder"

    def parser_clone(self, parser):
        parser.add_argument("repository", help="Repository to clone")

    def run_clone(self, args):
        toolsmanager.gitclone(args.repository)

    # ===== #
    # lsgit #
    # ===== #
    description_ls = "List all git repository installed with toolsmanager"

    def run_ls(self, args):
        toolsmanager.lsgit()

    # ======= #
    # gitpull #
    # ======= #
    description_pull = (
        "Update (pull) all github repositories installed with toolsmanager"
    )

    def parser_pull(self, parser):
        parser.add_argument(
            "rootpath", help="Folder containing git projects", nargs="?"
        )

    def run_pull(self, args):
        toolsmanager.gitpull(args.rootpath)

    # ====== #
    # rmgitt #
    # ====== #
    description_rm = "Remove a github repository installed with toolsmanager"

    def parser_rm(self, parser):
        parser.add_argument("project_name", help="Name of the git project to remove")

    def run_rm(self, args):
        toolsmanager.rmgit(args.project_name)


class ToolsmanagerSubcmdHelper(ArgparseSubcmdHelper):
    # class attributes
    autocomplete = True
    prog = "toolsmanager"
    description = "Toolsmanager helps managing tools and persistent env variables"
    # TODO: fix help with command_ in koalak
    sgroups = {
        "git": {
            "description": "Commands to manage git repositories",
            "commands": ["gitclone", "lsgit", "gitpull", "rmgit"],
        },
        "commands": {
            "description": "Commands to manage executables",
            "commands": ["addcmd", "rmcmd", "lscmd"],
        },
        "env variables": {
            "description": "command to manage environment variables",
            "commands": ["var"],
        },
    }

    description_var = "Manage persistant env variables"
    command_var = VarCommand

    description_cmd = "Manage commands"
    command_cmd = CmdCommand

    description_git = "Manage git tools"
    command_git = GitCommand

    description_version = "Show current version of Toolsmanager"

    def run_version(self, args):
        print("Toolsmanager current version:", consts.VERSION)

    # uninstall #
    # ========= #

    # install
    def parser_install(self, parser):
        parser.add_argument("toolname", help="Name of the tool to install", nargs="+")

    def run_install(self, args):
        toolnames = args.toolname

        plural_singular_tool = "tool" if len(toolnames) == 1 else "tools"
        coloring.print_info(
            f"Installing {coloring.bold(len(toolnames))} {plural_singular_tool}:",
            ", ".join(repr(e) for e in toolnames),
        )
        print()

        tm = get_current_toolsmanager()
        tm.install(*toolnames)

    # isinstalled
    def parser_isinstalled(self, parser):
        parser.add_argument("toolname", help="Name of the tool to install")

    def run_isinstalled(self, args):
        tm = get_current_toolsmanager()
        print(tm.isinstalled(args.toolname))

    # uninstall
    def parser_uninstall(self, parser):
        parser.add_argument("toolname", help="Name of the tool to install", nargs="+")

    description_uninstall = "Remove all git projects, variables, aliases and commands"

    def run_uninstall(self, args):
        toolnames = args.toolname

        plural_singular_tool = "tool" if len(toolnames) == 1 else "tools"
        coloring.print_info(
            f"Uninstalling {coloring.bold(len(toolnames))} {plural_singular_tool}:",
            ", ".join(repr(e) for e in toolnames),
        )

        tm = get_current_toolsmanager()
        tm.uninstall(*toolnames)

    def parser_howtoinstall(self, parser):
        parser.add_argument("toolname", help="Name of the tool to install", nargs="+")

    def run_howtoinstall(self, args):
        toolnames = args.toolname
        tm = get_current_toolsmanager()
        for tool in toolnames:
            tool = tm.get_tool(tool)
            for task in tool.tasks:
                print(task.howtoinstall())
        pass

    def run_list(self, args):
        tm = get_current_toolsmanager()
        for tool in tm.list():
            print(tool)

    def parser_status(self, parser):
        parser.add_argument("toolname", help="Name of the tool to install", nargs="+")

    def run_status(self, args):
        tm = get_current_toolsmanager()
        tm.status(*args.toolname)


def main():
    ToolsmanagerSubcmdHelper().run()


if __name__ == "__main__":
    main()
