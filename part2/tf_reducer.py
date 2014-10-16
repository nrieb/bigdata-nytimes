#!/usr/bin/env python
"""Takes word,id\t1 and gives back word,id \t tf"""

from __future__ import print_function
import sys

#   is_int :: String -> Bool
def is_int(string):
    """Determines if string is formed like int"""
    try:
        int(string)
    except ValueError:
        return False
    return True

#   main :: IO ()
def main():
    """main processor"""
    prev_key = None
    term_freq = 0
    key = None
    for line in sys.stdin:
        line = line.strip()
        key, count = line.split('\t', 1)
        if prev_key and prev_key != key:
            print("{0}\t{1}".format(prev_key, term_freq))
            term_freq = 0

        if is_int(count):
            term_freq += int(count)
            prev_key = key

    if term_freq and key:
        print("{0}\t{1}".format(prev_key, term_freq))

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
