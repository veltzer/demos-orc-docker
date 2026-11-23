#!/usr/bin/env python3

"""
Simple python logging applcation
"""

import os
import sys
import time

name = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("NAME", "mark")

i = 0
while True:
    print(f"hello {name} from python inside docker! ({i})")
    sys.stdout.flush()
    time.sleep(5)
    i = i+1
    if i == 4:
        raise ValueError("Help! I'm crashing...")
