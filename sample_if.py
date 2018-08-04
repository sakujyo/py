def test_if():
    d = {1: 2}
    print("d: {}".format(d))
    if True:
        pass
    if not 2 in d:
        print("not 2 in d")

if __name__ == '__main__':
    test_if()
