

def f():
    return 4


try:
    def test_func():
        assert f() == 3

finally:
    print('the end')




