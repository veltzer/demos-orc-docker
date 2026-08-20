#!/usr/bin/env python3

"""
This is the solution to the volumes exercise
"""

import os
import sys
import time


def main():
    """ main entry point """
    while True:
        print(f"I am [{os.getuid()}]")
        sys.stdout.flush()
        time.sleep(1)


if __name__ == "__main__":
    main()
