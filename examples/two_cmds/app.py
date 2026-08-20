#!/usr/bin/env python3

"""
Simple logging application
"""

import sys
import time

for i in range(5):
    print(f"hello from python inside docker! ({i}) {sys.argv}")
    time.sleep(1)
