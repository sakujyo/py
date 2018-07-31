import json

def test_jsonload():
    j = json.loads('{"table": "order"}')
    print(type(j), j)

if __name__ == '__main__':
    test_jsonload()
