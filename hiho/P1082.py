# -*- coding:utf-8 -*-


def main():
    while True:
        try:
            str = raw_input()
            for i in range(0, len(str)):
                sub_str = str[i:i+9]
                if sub_str.lower() == 'marshtomp':
                    str = str[:i] + 'fjxmlhx' + str[i+9:]
            print(str)
        except EOFError:
            break


if __name__ == '__main__':
    main()