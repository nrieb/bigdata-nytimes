#!/usr/bin/env python
"""Gets (url, num) and returns (_,num)"""

from __future__ import print_function
import sys
import json

#   is_int :: String -> Bool
def is_int(string):
    """Determines if string is formed like int"""
    try:
        int(string)
    except:
        return False
    return True

#   main :: IO ()
def main():
    """main processor"""
    curr_count = 0
    for line in sys.stdin:
        _, count = line.split('\t', 1)
        if is_int(count):
            curr_count += int(count)
        else:
            continue
    print("_\t{0}".format(curr_count))

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
