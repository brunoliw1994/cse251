import time
import threading
from plots import Plots
import random

START = 0
END = 100_000_001
LAUNCH_CODE = random.randint(START, END)
FOUND = False

def guess_code(start, end) -> None:
    global FOUND
    # Loop from start to end and find launch code
    for i in range(start, end):
        if not FOUND:
            if i == LAUNCH_CODE:
                print('Global Thermonuclear War Initiated')
                FOUND = True
                return
        else:
            return

def main() -> None:
    
    num_threads = 10
    yaxis = []
    
    number_threads = [1, 10, 25, 50, 100]
    for num_t in number_threads:
        global FOUND
        FOUND = False
        begin_time = time.time()
        increment = END // num_t
        threads = []
        
        for i in range(START, END, increment):
            # TODO create a thread, start it, call a function that takes a start and end number
            thread_end_number = i + increment
            #print(f'{i=}, {thread_end_number=}')
            t = threading.Thread(target=guess_code, args=(i, thread_end_number))
            t.start()
            threads.append(t)
        
        # Need to wait for threads to finish finding launch code
        for t in threads:
            t.join()
        
        total_time = round(time.time() - begin_time, 3)
        print(f'Total time = {total_time} sec')
        yaxis.append(total_time)
        
    plot = Plots()
    plot.line(number_threads, yaxis)

if __name__ == '__main__':
    print('BEGIN')
    main()