def add(a,b):
    c =(a-b)
    logging.info(f"Result: {c}")
    logging.info("This is from Pipeline -1")
    return c

def test_add():
    assert add(10,14) == -4
