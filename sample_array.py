from array import array

def test_array():
    z1000 = (0 for i in range(1000))
    #print(len(list(z1000)))
    a = array('L', (0 for i in range(1000)))
    #print(len(a), a)
    for i in range(1000):
        a[i] = i
    print("a[0], a[999]: {0}, {1}".format(a[0], a[999]))

if __name__ == '__main__':
    test_array()
