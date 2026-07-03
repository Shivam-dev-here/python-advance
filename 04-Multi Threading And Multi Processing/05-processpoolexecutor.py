# Multi Processing With Thread Pool Executor
# Use: Automatic handles (create, start, join) threads also reusable

from concurrent.futures import ProcessPoolExecutor
import time

def print_pent(val):
    time.sleep(1)
    return f"Quad: {val*val*val*val*val}"

val = [233,1232,131231,1322,1233,12333,133331,13333,111166,1234]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_pent, val)

    for result in results:
        print(result)