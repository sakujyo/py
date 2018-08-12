import sys, os, time

def test_try_except():
    it = iter(range(3))
    while True:
        try:
            n = next(it)
            print(n)
        except StopIteration:
            print("catched")
            quit()

if __name__ == '__main__':
    sys.stderr.write('pid: {}\n'.format(os.getpid()))
    test_try_except()
    sys.stderr.write('process_time: {}\n'.format(time.process_time()))
