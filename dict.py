'''
python - How do I sort a dictionary by value? - Stack Overflow
https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
'''
def test_dict():
    d = {1: 0}
    d[2] = 3
    print(type(d), d)
    for k, v in d.items():
        print("{0}: {1}".format(k, v))
    s = sorted(d.items(), key=lambda kv: -kv[1])
    print(type(s), s)
    for k, v in s:
        print("{0}: {1}".format(k, v))

if __name__ == '__main__':
    test_dict()
