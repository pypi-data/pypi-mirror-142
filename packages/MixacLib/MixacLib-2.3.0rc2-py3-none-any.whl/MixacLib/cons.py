from colorama import Fore
import os


def inf(information: str):
    """
    :param information: 输出信息
    :return:
    """
    green = Fore.GREEN
    reset = Fore.RESET
    print('[' + green + '信息' + reset + ']' + information)
    pass


def debug(debuginf: str):
    """
    :param debuginf: 调试信息
    :return:
    """
    cyan = Fore.CYAN
    reset = Fore.RESET
    print('[' + cyan + '调试' + reset + ']' + debuginf)
    pass


def warn(warning):
    """
    :param warning: 警告信息
    :return:
    """
    yellow = Fore.YELLOW
    reset = Fore.RESET
    print('[' + yellow + '警告' + reset + ']' + warning)
    pass


def error(errorinf):
    """
    :param errorinf: 错误信息
    :return:
    """
    red = Fore.RED
    reset = Fore.RESET
    print('[' + red + '错误' + reset + ']' + errorinf)
    pass


def title(titlestr):
    """
    :param titlestr: 标题信息
    :return:
    """
    magenta = Fore.MAGENTA
    reset = Fore.RESET
    print(magenta + titlestr + reset)


def console_title(name):
    """
    设置控制台标题
    :param name: 要设置的控制台标题
    :return:
    """
    os.system(f"title {name}")


def pause():
    """
    按任意键继续
    :return:
    """
    os.system("pause")


def clear():
    """
    清除控制台内容
    :return:
    """
    os.system("cls")


if __name__ == '__main__':
    inf("nmsl")
    pass
