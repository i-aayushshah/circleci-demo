from main import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(5, 5) == 10
    print("Add function works correctly")

def test_subtract():
    assert subtract(5, 2) == 3
    print("Subtract function works correctly")

if __name__ == '__main__':
    test_add()
    test_subtract()