import platform


def get_system():
    """
    获取系统信息
    :return: 返回一个包含系统架构和核心、设备网络名称、系统信息、CPU信息和系统版本的字典
    """
    get = {
        "arch": platform.architecture(),
        "node": platform.node(),
        "platform": platform.platform(),
        "CPU": platform.processor(),
        "os": platform.version()
    }
    return get


if __name__ == '__main__':
    print(get_system())
