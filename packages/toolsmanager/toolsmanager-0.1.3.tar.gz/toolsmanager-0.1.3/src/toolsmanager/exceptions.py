class ToolsManagerException(Exception):
    pass


class CmdAlreadyExistException(ToolsManagerException):
    pass


class CmdDontExistException(ToolsManagerException):
    pass


class ToolDontExistsException(ToolsManagerException):
    pass


class ToolAlreadyExistsException(ToolsManagerException):
    pass


class TasksInstallRequiresRootException(ToolsManagerException):
    pass


class TasksToolsInstallRequiresRootException(ToolsManagerException):
    pass
