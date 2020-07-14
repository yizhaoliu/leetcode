import time
def timer(func):
    def call_func(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        run_time = end - start
        print("用时%s秒"%run_time)
    return call_func

if __name__ == '__main__':
    @timer
    def test(a,b):
        result = a + b
        print('两数和为%s'%result)
        time.sleep(2)
    test(5 , 5)