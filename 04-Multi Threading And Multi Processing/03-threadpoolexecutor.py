# Multithreading With Thread Pool Executor
# Use: Automatic handles (create, start, join) threads also reusable

from concurrent.futures import ThreadPoolExecutor
import time

def print_quad(val):
    time.sleep(1)
    return f"Quad: {val*val*val*val}"

val = [233,1232,131231,1322,1233,12333,133331,13333,111166,1234]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_quad, val)

for result in results:
    print(result)