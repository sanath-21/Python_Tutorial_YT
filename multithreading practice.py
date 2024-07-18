import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    # Normal Code
    # time1 = time.perf_counter()
    # func(4) 
    # func(2)
    # func(1)
    # time2 = time.perf_counter()
    # print(time2-time1)

    # Same Code using threads
    time1 = time.perf_counter()
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()   #if you want to wait for the process to complete
    t2.join()   #if you want to wait for the process to complete
    t3.join()   #if you want to wait for the process to complete

    time2 = time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3) 
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [3,5,1,2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()