import time
import threading

def print_numbers():
    for num in range(5):
        time.sleep(2)
        print(f"Number is: {num}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter is: {letter}")

# Creating Thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# Start Threads
t1.start()
t2.start()

# Wait for Thread to complete

t1.join()
t2.join()

print(f"Finished Time: {time.time()-t}")