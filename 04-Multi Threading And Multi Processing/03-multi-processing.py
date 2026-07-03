# Multi Processing: Paraller execution, i.e. uses multiple cores
# Use: Cp-bound task (heavy cpu load)

import multiprocessing
import time

print("start")

def sq_num():
    for num in range(5):
        time.sleep(1)
        print(f"Sq of {num} is: {num*num}")

def cube_num():
    for num in range(5):
        time.sleep(1.3)
        print(f"Cube of {num} is: {num*num*num}")

if __name__=="__main__":

    # Creating multi processes
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)

    t=time.time()

    # Start the Processes
    p1.start()
    p2.start()

    # Wait for process to complete
    p1.join()
    p2.join()

    print(time.time()-t)
