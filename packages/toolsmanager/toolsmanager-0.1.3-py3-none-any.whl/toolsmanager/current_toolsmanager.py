from .dbtools import ToolsManager
from .utils import get_data_path


def get_current_toolsmanager():
    dbpath = get_data_path("dbtools", "tools.json")
    toolsmanager = ToolsManager()
    toolsmanager.loaddb(dbpath)
    return toolsmanager
