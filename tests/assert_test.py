

def f():
    return 3


try:
    def test_func():
        assert (f() == 3)

finally:
    print('the end')




