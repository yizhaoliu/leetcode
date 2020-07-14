import threading
import time
# 第一个线程，打印你
def threada():
    while True:
        lockb.acquire()
        print("你"),
        locka.release()
        time.sleep(0.2)


# 第二个线程，打印好
def threadb():
    while True:
        locka.acquire()
        print("好"),
        lockb.release()
        time.sleep(0.2)


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()
    
    ta = threading.Thread(target=threada)
    tb = threading.Thread(target=threadb)

    locka.acquire()  # 保证a先执行

    ta.start()
    tb.start()