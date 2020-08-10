import multiprocessing
import os


def run_proc(name):
    print("Child process {0} {1} Running".format(name, os.getpid()))


if __name__ == '__main__':
    print("Parent process {0} is running".format(os.getpid()))  # os.getpid()获取当前进程id
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))  # 创建一个进程，target执行函数，args函数参数
        print('process start')
        p.start()  # 启动进程
    p.join()  # 进程同步
    print("Process close")
