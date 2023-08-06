import time


def print_cur_time():
    ticks = time.time()
    localtime = time.localtime(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    print_cur_time()
