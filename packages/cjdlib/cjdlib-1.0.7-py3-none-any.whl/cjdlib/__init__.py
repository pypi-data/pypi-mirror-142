import time
import psutil
import platform
import os
import socket
from psutil._common import bytes2human
from time import sleep
from rich.progress import track

name = "cjdlib"
print("Welcome to cjdlib!")


def print_the_time():
    """_summary_
    """
    while True:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)


def decomposed_prime_factor(num: int):
    """_summary_

    Args:
        num (int): _description_
    """
    m = []
    while num != 1:  # n==1时，已分解到最后一个质因数
        for i in range(2, int(num + 1)):
            if num % i == 0:
                m.append(str(i))  # 将i转化为字符串再追加到列表中，便于使用join函数进行输出
                num = num / i
        if num == 1:
            break  # n==1时，循环停止
    print('×'.join(m))


class bcolors:
    """_summary_
    """
    # 颜色输出
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_disk_space(path: str) -> tuple:
    """_summary_

    Args:
        path (str): _description_

    Returns:
        tuple: _description_
    """
    usage = psutil.disk_usage(path)
    space_total = bytes2human(usage.total)
    space_used = bytes2human(usage.used)
    space_free = bytes2human(usage.free)
    print(f"总容量：{space_total}\n已用：{space_used}\n剩余：{space_free}")
    return space_total, space_used, space_free


def get_os_info():
    """_summary_
    """
    def showinfo(tip, info):
        print("{}:{}".format(tip, info))

    showinfo("操作系统及版本信息", platform.platform())
    showinfo('获取系统版本号', platform.version())
    showinfo('获取系统名称', platform.system())
    showinfo('系统位数', platform.architecture())
    showinfo('计算机类型', platform.machine())
    showinfo('计算机名称', platform.node())
    showinfo('处理器类型', platform.processor())
    showinfo('计算机相关信息', platform.uname())
    showinfo('python相关信息', platform.python_build())
    showinfo('python版本信息:', platform.python_version())


def get_time_of_the_year(year: str, month: str, day: str) -> None:
    """_summary_

    Args:
        year (str): _description_
        month (str): _description_
        day (str): _description_
    """
    read_time = year + '-' + month + '-' + day
    stru_time = time.strptime(read_time, r'%Y-%m-%d')
    print('这一天是这一年的第', stru_time.tm_yday, '天')


def print_all(*string, times: float = 0.1, line_feed: bool = False):
    """_summary_

    Args:
        string (_type_): _description_
        times (float, optional): _description_. Defaults to 0.1.
        line_feed (bool, optional): _description_. Defaults to False.
    """
    if line_feed is True:
        print("\n")
    for strs in string:
        for astr in strs:
            sleep(times)
            print(strs, end='', flush=True)


def countdown_day(day: str) -> str:
    """_summary_

    Args:
        day (str): _description_

    Returns:
        str: _description_
    """
    t = abs(time.mktime(time.strptime(day, "%Y-%m-%d %H:%M:%S")) - time.time())
    d = int(t // 86400)
    H = int(t % 86400 // 3600)
    M = int(t % 3600 // 60)
    S = int(t % 60)
    n = "距离目标还有{}天{}小时{}分钟{}秒".format(str(d), str(H), str(M), str(S))
    return n


def prime_number(num: int) -> bool:
    """_summary_

    Args:
        num (int): _description_

    Returns:
        bool: _description_
    """
    x = True
    for n in range(2, num):
        if num % n == 0:
            x = False
            return False
    if x is True:
        return True


def perfect_number(num: int) -> bool:
    """_summary_

    Args:
        num (int): _description_

    Returns:
        bool: _description_
    """
    x = 0
    for n in range(1, num):
        if num % n == 0:
            x += n
        if x > num:
            return False
    if num == x:
        return True
    else:
        return False


def find_file_by_suffix(suffix: str, path: str = os.getcwd()) -> list:
    """_summary_

    Args:
        suffix (str): _description_
        path (str, optional): _description_. Defaults to os.getcwd().

    Returns:
        list: _description_
    """
    file_list = os.listdir(path)
    for file in file_list:
        if file[-3:] != suffix:
            file_list.remove(file)
    file_path = []
    for file in file_list:
        file_path.append(os.path.join(path, file))
    return file_path


def get_host_ip() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8", 80))
        ip = s.getsockname()[0]
    return ip


def progress_bar(time=0.2):
    """_summary_

    Args:
        time (float, optional): _description_. Defaults to 0.2.
    """
    for step in track(range(100)):
        time.sleep(time)
