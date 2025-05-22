def add(a,b):
    c =(a-b)
    print(c)
    print("This is from Pipeline -1")
    return c

def test_add():
    assert add(10,14) == -4
