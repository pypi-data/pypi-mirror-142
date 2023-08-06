PATH=$$PATH:$TM_BIN
TM_BIN=$TM_BIN
TM_HOME=$home
TM_GIT=$TM_GIT

. $vars_path
. $alias_path


# If we are not root add the files for root
if [[ $$EUID -ne 0 ]]; then
   if [ -d /toolsmanager/ ]; then
      PATH=$$PATH:/toolsmanager/bin
      . /toolsmanager/vars.sh
      . /toolsmanager/alias.sh
   fi
fi
