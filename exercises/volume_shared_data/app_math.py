#!/usr/bin/env python3

"""
logging app that can receive sleep time and interval
"""

import os.path
import time

# import random  # noqa: ERA001  teaching: kept in the comment for the reader
# import sys  # noqa: ERA001  teaching: kept in the comment for the reader


def main():
    """ main entry point """
    filename = "data/data.txt"

    # no parameters
    # sleep_time=random.randint(2,7)  # noqa: ERA001  teaching: kept in the comment for the reader
    # increment=random.randint(2,7)  # noqa: ERA001  teaching: kept in the comment for the reader
    # command line
    # sleep_time = int(sys.argv[1])  # noqa: ERA001  teaching: kept in the comment for the reader
    # increment = int(sys.argv[2])  # noqa: ERA001  teaching: kept in the comment for the reader
    # environment
    sleep_time = int(os.environ["SLEEP_TIME"])
    increment = int(os.environ["INCREMENT"])
    print("=================================")
    print(f"sleep_time is {sleep_time}")
    print(f"increment is {increment}")
    print("=================================")

    mode = "a+" if os.path.isfile(filename) else "w+t"

    i = 0
    with open(filename, mode, encoding="utf-8") as stream:
        while True:
            stream.seek(0)
            lines = stream.readlines()
            if lines:
                i = int(lines[-1])
            print(f"incrementing by {increment} the value {i}")
            i += increment
            stream.write(f"{i}\n")
            stream.flush()
            print(f"sleeping for {sleep_time}")
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
