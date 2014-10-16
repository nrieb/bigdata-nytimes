#!/usr/bin/env python
"""word \t id,tf from word,id \t tf"""
from __future__ import print_function
import sys

def main():
    """main function"""
    for line in sys.stdin:
        line = line.strip()
        key, term_freq = line.split("\t", 1)
        word, ident = key.split(",", 1)
        print("{word}\t{ident},{tf}".format(ident=ident,
                                            word=word,
                                            tf=term_freq))


"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
