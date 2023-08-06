import base64


def verify_with_base64(str1, str2):
    """

    :param str1: 明文
    :param str2: 密文
    :return:
    """
    str1_enc = str1.encode('utf-8')
    b64 = base64.b64encode(str1_enc)

    return str2 == b64


if __name__ == '__main__':
    f = verify_with_base64('114514', base64.b64encode('114514'.encode('utf-8')))
    print(f)
