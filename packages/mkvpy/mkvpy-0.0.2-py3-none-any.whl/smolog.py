import os
from inspect import getframeinfo, stack
from datetime import datetime

class bcolors:
    PINK = '\033[95m'
    PURPLE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = "\033[91m"
    GREY = "\033[90m"
    ENDC = '\033[0m'

colors = [bcolors.GREY, bcolors.RED, bcolors.PINK, bcolors.PURPLE, bcolors.CYAN, bcolors.GREEN, bcolors.YELLOW]

CRITICAL = "CRITICAL"
INFO = "INFO"
DEBUG = "DEBUG"
ALL = "ALL"

scope_to_level = {}
scope_to_level[CRITICAL] = 3
scope_to_level[INFO] = 2
scope_to_level[DEBUG] = 1
scope_to_level[ALL] = 0

SCOPE = "LOG_SCOPE"

if SCOPE in os.environ.keys():
    log_scope = os.environ[SCOPE]
else:
    log_scope = ALL

log_levels = scope_to_level.keys()

# try catch to make sure that log cannot break runtime of programs that log

def log(*args, level=DEBUG, depth=0, **kwargs):
    try:
        caller = getframeinfo(stack()[1+depth][0])
        if level not in log_levels:
            print("Got log level [{}], expected one of {}".format(
                level, log_levels))
            print("Message that was attempted to be printed was {}".format(args))
            return
        local_lev = scope_to_level[level]
        lev = scope_to_level[log_scope]
        if lev <= local_lev:
            now = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S.%f")
            pid = os.getpid()
            color_index = pid % len(colors)
            print(colors[color_index] + "[%d %s] %s:%d:" % (pid, now, caller.filename.split(
                "/")[-1], caller.lineno), *args, bcolors.ENDC, **kwargs)
    except Exception as e:
        print("Failed to log [{}]".format(e))

def make_logger(level):
    def wrap(*args, **kwargs):
        log(*args, level=level, depth=1, **kwargs)
    return wrap

info = make_logger(level="INFO")
critical = make_logger(level="CRITICAL")
debug = make_logger(level="DEBUG")

if __name__ == "__main__":
    info = make_logger("INFO")
    info("test log")
    info("test2")
    for c in colors:
        info(c, "yo", bcolors.ENDC)
