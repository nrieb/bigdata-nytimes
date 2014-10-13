#!/usr/bin/env python
"""Takes json record and prints out the url for each record (url\t1) style"""

from __future__ import print_function
import sys
import json

#   main :: IO ()
def main():
    """main processor"""
    for line in sys.stdin:
        record = json.dumps(line)
        if "url" in record:
            print("{0}\t1".format(record["line"]))

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
