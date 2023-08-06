from .bases import fw_toolsmanager
from .current_toolsmanager import get_current_toolsmanager
from .dbtools import ToolsManager
from .functions import (
    addcmd,
    addvar,
    clearcmd,
    clearvar,
    gitclone,
    gitpull,
    install,
    isinstalled,
    lscmd,
    lsgit,
    lsvar,
    rmcmd,
    rmgit,
    rmvar,
    uninstall,
)

__all__ = [
    "fw_toolsmanager",
    "lscmd",
    "addcmd",
    "lsvar",
    "rmcmd",
    "clearcmd",
    "clearvar",
    "lsgit",
    "gitclone",
    "gitpull",
    "rmgit",
    "rmvar",
    "addvar",
    "install",
    "isinstalled",
    "uninstall",
    "get_current_toolsmanager",
    "ToolsManager",
]
# TODO: replace print with errors? to be used as library
