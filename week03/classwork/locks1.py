import threading
import time
import random

VALUE = 10

def adder(amount: int, repeat_amount: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeat_amount):
        #with lock:
        lock.acquire()
        tmp = VALUE
        tmp += amount
        time.sleep(random.uniform(0.0001, 0.001))
        VALUE = tmp
        #raise Exception("stop")
        lock.release()

def subtractor(amount: int, repeat_amount: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeat_amount):
        #with lock:
        #print(f'{threading.current_thread().name}: acquiring lock')
        lock.acquire()
        #print(f'{threading.current_thread().name}: acquired lock')
        tmp = VALUE
        tmp -= amount
        time.sleep(random.uniform(0.0001, 0.001))
        VALUE = tmp
        lock.release()

def main():
    
    lock = threading.Lock()
    t1 = threading.Thread(target=adder, args=(1, 1000, lock))
    t1.start()
    
    t2 = threading.Thread(target=subtractor, args=(1, 1000, lock))
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f'\n{VALUE=}')

if __name__ == '__main__':
    main()