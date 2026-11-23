#!/usr/bin/env python3

"""
A writer that continues to write where it left off
"""

import os.path
import sys
import time


def main():
    """ main function """
    filename = "/data/data.txt"

    if os.path.isfile(filename):
        with open(filename, encoding="utf-8") as stream:
            lines = stream.readlines()
            i = int(lines[-1] if lines else "0") + 1
    else:
        i = 0
    with open(filename, "a", encoding="utf-8") as stream:
        while True:
            stream.write(f"{i}\n")
            stream.flush()
            print("just wrote {i}...")
            sys.stdout.flush()
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    main()
