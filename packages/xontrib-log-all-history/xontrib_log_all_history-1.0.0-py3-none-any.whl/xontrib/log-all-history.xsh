import os
__all__ = ()

if "LOG_DESTINATION" not in ${...}:
    $LOG_DESTINATION="{}/.logs".format($HOME)

def init():
    if $XONSH_HISTORY_BACKEND == 'json':
        from xonsh.history.json import JsonHistory
        class HistoryProxy(JsonHistory):
            pass
    elif $XONSH_HISTORY_BACKEND == 'sqlite':
        from xonsh.history.sqlite import SqliteHistory
        class HistoryProxy(SqliteHistory):
            pass
    else:
        return

    class SaveAllHistory(HistoryProxy):
        def append(self, cmd):
            try:
                cwd = "{}{}".format($LOG_DESTINATION, $PWD)
                if not os.path.exists(cwd):
                    os.makedirs(cwd)
                file = "{}/xonsh-history-{}.log".format(cwd, datetime.now().strftime("%Y-%m-%d"))
                open(file, "a").write("{} {}".format(datetime.now().strftime("%Y-%m-%d.%H.%M.%S"), cmd["inp"]))
                super().append(cmd)
            except Exception:
                print("History not being saved")
    $XONSH_HISTORY_BACKEND = SaveAllHistory

    aliases['hgrep'] = lambda args: execx('grep -Rh {} {}'.format(repr(args[0]), $LOG_DESTINATION))
    aliases['hdgrep'] = lambda args: execx('grep -Rh {} {}'.format(repr(args[0]), $LOG_DESTINATION + $PWD))
init()
