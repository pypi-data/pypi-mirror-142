from datetime import datetime
from math import sqrt
from time import perf_counter, sleep

from win32gui import GetWindowText, GetForegroundWindow, FindWindow


# Math Functions
def safe_div(x, y):
    return 0 if y == 0 else x / y


def safe_div_round(x, y, decimals=2):
    return round(safe_div(x, y), decimals)


def safe_div_int(x, y):
    return int(0 if y == 0 else x / y)


def get_distance(p0, p1):
    return sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


# Process Functions
def get_handle(window):
    return FindWindow(None, window)


def current_window():
    return GetWindowText(GetForegroundWindow())


def is_current_window(window_name: str):
    return window_name == current_window()


def pause(milliseconds: int):
    sleep(milliseconds * 0.001)


def make_hash(d):
    __ = ''
    for _ in d:
        __ += str(d[_])
    return hash(__)


# Utility Functions
def timestamp():
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d-%H%M%S.%f').split('.')
    dt = "%s.%03d" % (dt, int(micro) * 0.001)
    return dt


def perf():
    return perf_counter()


# I/O
def write_to_file(filename, text, method: str = "a", add_new_line: bool = True):
    with open(filename, method) as file:
        if add_new_line:
            file.write(text + "\n")
        else:
            file.write(text)


def read_file(filename, method="r"):
    return open(filename, method).read()


def read_lines(filename, method="r"):
    return open(filename, method, encoding="utf8").readlines()


# Assorted
def cv_q_stop(cv2):
    if cv2.waitKey(200) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
