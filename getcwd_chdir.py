# https://qiita.com/Oz-Spade/items/7fa479fae7a0ea6fcddf
import os
import time

def test_getcwd():
    print("pid: {}".format(os.getpid()))
    print(os.getcwd())
    os.chdir('C:\\tmp')
    print(os.getcwd())
    print(dir(os))
    print(time.process_time())

if __name__ == '__main__':
    test_getcwd()
