import json
from typing import List

import attr
import coloring

from . import consts, exceptions, utils
from .bases import pm_tasks
from .consts import IsInstalledStatus
from .printer import printer

# Import to load tasks
from .tasks import BaseTask


@attr.s
class Collection:
    name = attr.ib()
    collections = attr.ib(kw_only=True, factory=list)
    tools = attr.ib(kw_only=True, factory=list)


@attr.s
class AttrTool:
    name = attr.ib()
    deps = attr.ib(kw_only=True, factory=set)
    tasks: List[BaseTask] = attr.ib(kw_only=True, factory=list)
    tags = attr.ib(kw_only=True, factory=set)
    toolsmanager = attr.ib(kw_only=True)

    def _install_tasktools(self, printer=printer):
        """Install tasktools required (apt, git, bin, ...)"""

        # Printing
        tasktools_installed = self.are_tasktools_installed()

        # Debug: status of tasktools
        printer.debug(
            repr(self.name),
            "are tasktools installed",
            [e.name for e in self.get_tasktools()],
            tasktools_installed.name,
        )

        # If all tasktools are installed, do nothing
        if tasktools_installed == IsInstalledStatus.YES:
            printer.info(
                "TaskTools required installed", [e.name for e in self.get_tasktools()]
            )
            return

        # If we are not root, check that we can install anyway
        if not consts.is_root:
            for tool in self.get_tasktools():
                if tool.isinstalled() != IsInstalledStatus.YES and tool.requires_root():
                    coloring.print_failure(
                        "TaskTool not installed and requires root", tool.name
                    )
                    raise exceptions.TasksToolsInstallRequiresRootException

        # Install tasktools
        tasktools = self.get_tasktools()
        if tasktools:
            printer.info("Installing TaskTools", [tool.name for tool in tasktools])
            printer.indent()
            for tool in self.get_tasktools():
                # Install is responsible to check if the tool is installed
                if tool.isinstalled() != IsInstalledStatus.YES:
                    tool.install()
            printer.dedent()
        else:
            printer.info("No tasktools required")

    def _install_deps(self, printer=printer):
        if not self.deps:
            printer.info("No dependencies are required")
            return

        deps_installed = self.are_deps_installed()
        printer.debug("Deps installed", deps_installed.name)
        if deps_installed == IsInstalledStatus.YES:
            printer.info(
                "Dependencies are installed", [tool.name for tool in self.deps]
            )
            return

        # If we are not root, check that we can install anyway
        if not consts.is_root:
            for tool in self.deps:
                if tool.isinstalled() != IsInstalledStatus.YES and tool.requires_root():
                    coloring.print_failure(
                        "Deps not installed and requires root", tool.name
                    )
                    # FIXME: raise the good exception (dep not tasktool)
                    raise exceptions.TasksToolsInstallRequiresRootException

        # install deps
        printer.info("Installing dependencies", [tool.name for tool in self.deps])
        printer.indent()
        for tool in self.deps:
            # Install is responsible to check if the tool is installed
            if tool.isinstalled() != IsInstalledStatus.YES:
                tool.install()
        printer.dedent()
        printer.info("Dependencies installed", [tool.name for tool in self.deps])
        # TODO: check root/nanani nananar

    def install(self, *, printer=printer):
        printer.info("Installing", self.name)
        # Verify if TaskTools (git, apt, ...)for this tool are installed
        self._install_tasktools(printer=printer)

        # Check dependencies
        self._install_deps(printer)

        # FIXME: check is installed before root previlges
        is_installed = self.isinstalled()
        # Tool already installed => do nothing
        if is_installed == IsInstalledStatus.YES:
            printer.info(f"{self.name} is already installed")
            return
        elif is_installed == IsInstalledStatus.NO:
            printer.verbose(f"{self.name} is not installed")
        else:
            printer.info(f"{self.name} is installed status {is_installed.name!r}")

        requires_root = self.tasks_requires_root()

        # debug printing
        if requires_root:
            printer.verbose(f"{self.name!r} requires root privileges to be installed")
        else:
            printer.verbose(
                f"{self.name!r} does not require root privileges to be installed"
            )

        # exit if not root and need root privileges (like with sudo apt install)
        if requires_root and not utils.is_root():
            printer.verbose(f"{self.name!r} requires root privileges to be installed")
            raise exceptions.TasksInstallRequiresRootException

        # check if the tool is installed

        # install
        printer.info("Starting", self.name, "installation")
        # FIXME: we already checked installs, gather the i of last installed and go on
        # TODO: Install deps
        # Create metadata to give to all tasks
        meta = {}
        # Keep track of previous_tasks
        previous_tasks = []
        for task in self.tasks:
            is_installed = task.isinstalled()
            if not is_installed == IsInstalledStatus.YES:
                # prepare for installation (meta, previous_tasks)
                # keep old meta
                old_meta = task.meta
                task.meta = dict(task.meta)
                task.meta.update(meta)

                # keep old previous_tasks
                old_previous_tasks = task.previous_tasks
                task.previous_tasks = previous_tasks

                # install
                task.install()

            meta = task.get_metadata()
            previous_tasks.append(task)

            if not is_installed == IsInstalledStatus.YES:
                # restore meta/previous_tasks
                task.meta = old_meta
                task.previous_tasks = old_previous_tasks

        printer.success(self.name, "installed")

    def isinstalled(self):
        if len(self.tasks) == 0:
            return IsInstalledStatus.YES
        # last one yes => yes
        #   no no no yes => yes (it's not normal to have the last installed and not the previous)

        # all yes => yes
        # yes yes dontknow => yes (if the last one is dontknow take
        # one no => no
        # TODO: fixme with DONTKNOW
        # FIXME: if one no, maybe previous tasks are yes (example in nikto (git+bin)
        #   bin is no but git is yes => is_installed => partial
        for i, task in reversed(list(enumerate(self.tasks))):
            is_installed = task.isinstalled()
            # print("[DEBUG]", task.name, is_installed.name)
            if is_installed == IsInstalledStatus.NO:
                return IsInstalledStatus.NO
            elif is_installed == IsInstalledStatus.YES:
                return IsInstalledStatus.YES
        return IsInstalledStatus.DONTKNOW

    def uninstall(self):
        is_installed = self.isinstalled()
        if is_installed == IsInstalledStatus.YES:
            coloring.print_info(f"{self.name!r} is already installed")
        elif is_installed == IsInstalledStatus.NO:
            coloring.print_info(f"{self.name!r} is not installed, skipping")
        else:
            coloring.print_info(
                f"{self.name!r} is installed status {is_installed.name!r}"
            )

        if is_installed in [IsInstalledStatus.YES, IsInstalledStatus.DONTKNOW]:
            for task in reversed(self.tasks):
                task.uninstall()

    def requires_root(self):
        return self.tasks_requires_root() or self.deps_requires_root()

    def tasks_requires_root(self):
        return any(task.requires_root() for task in self.tasks)

    def deps_requires_root(self):
        return any(tool.requires_root() for tool in self.deps)

    def deps_names(self):
        """Return the names of all dependencies"""
        return [tool.name for tool in self.deps]

    def not_installed_deps_requires_root(self):
        """Tells if the not installed dependencies (with the tasks) requires root"""
        for tool_dep in self.deps:
            print(
                "Tool dep",
                tool_dep.name,
                tool_dep.isinstalled(),
                tool_dep.requires_root(),
            )
            if (
                tool_dep.requires_root()
                and tool_dep.isinstalled() != IsInstalledStatus.YES
            ):
                print("Tool", self.name, "requires root")
                return True
            else:
                print("")
        print("Tool", self.name, "dont requires root")
        return False

    def are_tasktools_installed(self):
        # all yes => yes
        # one no => non
        for task in self.tasks:
            if not task.is_tasktool_installed() == IsInstalledStatus.YES:
                return IsInstalledStatus.NO
        return IsInstalledStatus.YES

    def are_deps_installed(self):
        # all yes => yes
        # one no => non
        for tool in self.deps:
            if not tool.isinstalled() == IsInstalledStatus.YES:
                return IsInstalledStatus.NO
        return IsInstalledStatus.YES

    def get_tasktools(self):
        """Return Tasktoools without duplication"""
        return [
            self.toolsmanager.get_tool(taskname)
            for taskname in self.get_tasktools_names()
        ]

    def get_tasktools_names(self):
        """Return tasktools names (apt, git, bin, ...) without duplication"""
        return utils.distinct_list([task.name for task in self.tasks])

    def status(self):
        print(f"Tool name", self.name)
        print(f"Deps", [e.name for e in self.deps])
        print(f"Tasks")
        for task in self.tasks:
            print(task.howtoinstall())
        print()
        print("Requires root")
        print("  Tasks", self.tasks_requires_root())
        print("  Deps", self.deps_requires_root())
        print("  All", self.requires_root())

        # Isinstalled
        print("Is installed")
        print("  Tool", self.isinstalled().name)
        print("  TaskTools", self.are_tasktools_installed().name)
        print("  Deps", self.are_deps_installed().name)

        print("TaskTools")
        for tool in self.get_tasktools():
            print(" ", tool)

        # Requires root privileges
        requires_root = self.requires_root()
        # debug printing
        if requires_root:
            coloring.print_info(
                f"{self.name!r} requires root privileges to be installed"
            )
        else:
            coloring.print_info(
                f"{self.name!r} does not require root privileges to be installed"
            )

        tasktools_installed = self.are_tasktools_installed()
        coloring.print_info("tasktools instlled", tasktools_installed)


class Tool:
    def __init__(self, name, *, raw_tasks):
        self.name = name
        self.raw_tasks = raw_tasks
        self._tasks = None

    @property
    def tasks(self):
        if self._tasks is None:
            self._tasks = []
            for raw_task in self.raw_tasks:
                raw_task = dict(raw_task)
                Task = pm_tasks[raw_task["task"]]
                kwargs = dict(raw_task)
                kwargs.pop("task")
                task = Task(**kwargs)
                self._tasks.append(task)
        return self._tasks

    def isinstalled(self):
        pass

    def install(self):
        pass

    def requires_root(self):
        return any(task.requires_root() for task in self.tasks)

    def __str__(self):
        return f"Tool({self.name!r})"

    def __repr__(self):
        return self.__str__()


class ToolsManager:
    def __init__(self):
        # Tools as class
        self._tools = {}
        # Tools in dict format
        self._raw_tools = {}

    def __getitem__(self, item) -> Tool:
        if item in self._tools:
            return self._tools[item]

        raw_tool = self._raw_tools[item]
        tool = Tool(raw_tool["name"], raw_tasks=raw_tool["tasks"])

        self._tools[item] = tool
        return tool

    def add_tool(self, name, *, tasks=None, deps=None, tags=None):
        if name in self._tools:
            raise exceptions.ToolAlreadyExistsException(
                f"Tool {name!r} already in database"
            )

        if tasks is None:
            tasks = []

        if deps is None:
            deps = []

        tasks = [self.normalize_task(task) for task in tasks]
        self._tools[name] = AttrTool(
            name, tags=tags, tasks=tasks, deps=deps, toolsmanager=self
        )

    def get_tool(self, name: str) -> AttrTool:
        return self._tools[name]

    def install(self, *toolnames, raise_errors=False, printer=printer):
        # TODO: fix order with set/list
        toolnames = set(toolnames)  # remove duplicates
        # nb_success = 0
        # nb_failures = 0
        for tool_name in toolnames:
            try:
                tool = self.get_tool(tool_name)
                tool.install(printer=printer)
                printer.print()
            except Exception as e:
                coloring.print_failure(
                    f'Error installing {tool_name!r} "{type(e).__name__} {e}"'
                )
                continue

    def uninstall(self, *toolnames, raise_errors=False):
        toolnames = set(toolnames)  # remove duplicates
        # nb_success = 0
        # nb_failures = 0
        for tool_name in toolnames:
            try:
                tool = self.get_tool(tool_name)
                coloring.print_info(f"Uninstalling {tool.name!r}")
                tool.uninstall()

            except Exception as e:
                coloring.print_failure(
                    f'Error uninstalling {tool_name!r} "{type(e).__name__} {e}"'
                )
                continue

    def status(self, *toolnames):
        for tool_name in toolnames:
            try:
                tool = self.get_tool(tool_name)
                coloring.print_info(f"Status {tool.name!r}")
                tool.status()
                print()

            except Exception as e:
                coloring.print_failure(
                    f'Error status {tool_name!r} "{type(e).__name__} {e}"'
                )
                continue

    def install_collection(self,):
        pass

    def isinstalled(self, toolname):
        tool = self.get_tool(toolname)
        return tool.isinstalled()

    def normalize_task(self, task) -> BaseTask:
        if isinstance(task, BaseTask):
            return task
        raw_task = task
        del task

        raw_task = dict(raw_task)  # make a copy
        Task = pm_tasks[raw_task["task"]]  # get the cls of the task
        kwargs = dict(raw_task)
        kwargs.pop("task")
        task = Task(**kwargs)
        task.toolsmanager = self

        return task

    def loaddb(self, dbpath: str):
        raw_json_tools = json.load(open(dbpath))

        for raw_tool in raw_json_tools:
            tasks = raw_tool.get("tasks", None)
            self.add_tool(
                raw_tool["name"],
                tasks=tasks,
                deps=raw_tool.get("deps"),
                tags=raw_tool.get("tags"),
            )

        # Load deps
        for toolname, tool in self._tools.items():
            tool.deps = [self.get_tool(dep) for dep in tool.deps]

    def loaddb_old(self, dbpath):
        # old function using lazy load (maby I will use it latter if needed)
        json_tools = json.load(open(dbpath))
        tools = {}
        for json_tool in json_tools:
            name = json_tool["name"]
            tools[name] = json_tool

        self._raw_tools = tools

    def list(self):
        tools = []
        for tool_name, tool in self._tools.items():
            tools.append({"tool": tool.name, "isinstalled": tool.isinstalled()})
        return tools
