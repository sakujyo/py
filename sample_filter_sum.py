import os

def test_filter_sum():
    l = [(1.001, 10), (1.002, 10), (1.003, 30), (1.007, 70)]
    proportions = list(map(lambda x: 1 + x, [0.0025, 0.005, 0.01]))
    zp = list(zip([1]+proportions, proportions))
    print("zp: {}".format(zp))
    standard = 1
    f0 = filter(lambda x: standard * zp[0][0] <= x[0] and x[0] < standard * zp[0][1], l)
    print(list(f0))
    fs = [sum(map(lambda kv: kv[1], filter(
        lambda x: standard * r[0] <= x[0] and x[0] < standard * r[1], l
        ))) for r in zp]
    print(fs)

if __name__ == '__main__':
    print("pid: {}".format(os.getpid()))
    test_filter_sum()
