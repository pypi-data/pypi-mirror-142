import psutil
import subprocess
import os

from typing import List


def proc_open(args: List[str], cwd: str = os.getcwd()):
    """
    启动新子线程（不阻塞主进程）
    必须导入subprocess
    :param args: 列表，第一项为可执行文件路径，之后为参数，无参数时可只有一项
    :param cwd: 运行目录，默认为当前程序目录
    :return: Subprocess Popen对象
    """
    p = subprocess.Popen(args, cwd=cwd)
    return p


def is_ended(process: subprocess.Popen):
    """
    检查进程退出状态
    :param process: Subprocess Popen对象
    :return: 返回p.returncode，None指尚未结束
    """
    return process.poll()
