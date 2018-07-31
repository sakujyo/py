# https://qiita.com/Oz-Spade/items/7fa479fae7a0ea6fcddf
import os

def test_getcwd():
    print(os.getpid())
    print(os.getcwd())
    os.chdir('C:\\tmp')
    print(os.getcwd())
    print(dir(os))

if __name__ == '__main__':
    test_getcwd()
