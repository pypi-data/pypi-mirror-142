from koalak import D, F, mkframework

from . import consts, utils

# fmt: off
home_structure = [
    D("git"),
    D("bin"),
    F(
        ".bashrc",
        src=utils.get_data_path("tm_bashrc.sh"),
        substitute=True,
        actions="bashrc"  # this file must be executed by bashrc
    ),
]
# fmt: on

fw_toolsmanager = mkframework(
    "toolsmanager",
    home_structure=home_structure,
    homepath=consts.TM_HOME,
    variables={"TM_BIN": consts.TM_BIN, "TM_GIT": consts.TM_GIT},
    version=consts.VERSION,
)

fw_toolsmanager.variables.set("vars_path", "$home/vars.sh", substitute=True)
fw_toolsmanager.variables.set("alias_path", "$home/alias.sh", substitute=True)

fw_toolsmanager.init()

fw_toolsmanager.create_dict_db("vars", path="$vars_path", type="txt", sep="=")

# FIXME: unique!
fw_toolsmanager.create_list_db(
    "alias", path="$alias_path", type="txt", unique=lambda x: x.split("=")[0]
)


pm_tasks = fw_toolsmanager.mkpluginmanager("tasks")


@pm_tasks.mkbaseplugin
class BaseTask:
    def __init__(self):
        self.previous_tasks = []
        self.meta = {}
        self.toolsmanager = None

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        return self.__str__()

    def requires_root(self):
        return False

    def get_metadata(self):
        return {}

    def uninstall(self):
        pass

    def isinstalled(self) -> consts.IsInstalledStatus:
        return consts.IsInstalledStatus.DONTKNOW

    def update(self):
        pass

    def howtoinstall(self) -> str:
        return self.__str__()

    def is_tasktool_installed(self):
        """If the Task tool (git, apt, ...) is installed"""
        return self.toolsmanager.get_tool(self.name).isinstalled()
