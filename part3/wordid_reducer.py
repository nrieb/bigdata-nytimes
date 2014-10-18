#!/usr/bin/env python
""" word \t docid,tfidf"""
from __future__ import print_function
import sys

def main():
    """main function"""
    for line in sys.stdin:
        print(line, end='')

"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
