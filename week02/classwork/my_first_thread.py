import threading
import time

#SUM = [0] * 3
SUM = []

class Sum_Thread(threading.Thread):
    def __init__(self, index: int, num1: int, num2: int) -> None:
        super().__init__()
        self.index = index
        self.num1 = num1
        self.num2 = num2
        self.result = 0
    
    def display(self):
        print(f'{self.result=}')
        
    def run(self):
        sum = self.num1 + self.num2
        self.result = sum
        #print(f'{threading.current_thread().name}: {sum}\n', end="")

def add_two_numbers(index: int, num1: int, num2: int):
    global SUM
    sum = num1 + num2
    time.sleep(1)
    print(f'{sum=}\n', end="")
    SUM.append(sum)
    # return sum


def main():

    threads = []
    # for i in range(3):
    #     t1 = threading.Thread(target=add_two_numbers, args=(i, 0, i))
    #     t1.start()
    #     threads.append(t1)

    # for t in threads:
    #     t.join()
    
    for i in range(3):
        t1 = Sum_Thread(i, 0, i)
        t1.start()
        threads.append(t1)
    
    for t in threads:
        t.join()
        #t.display()
        print(f'{t.result=}')
    #print(f'{SUM=}')


if __name__ == "__main__":
    main()
    print('Done')
