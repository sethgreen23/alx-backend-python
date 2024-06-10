#!/usr/bin/env python3
# countsync.py

import time

def count(index):
    print("One "+ str(index))
    time.sleep(1)
    print("Two "+ str(index))

def main():
    for i in range(3):
        count(i)

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
