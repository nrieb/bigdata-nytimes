#!/usr/bin/env python
"""word,docid \t tfidf -> word \t docid,tfidf"""
from __future__ import print_function
import sys

def main():
    """main function"""
    for line in sys.stdin:
        line = line.strip()
        key, tfidf = line.split("\t", 1)
        word, ident = key.split(",", 1)
        print("{word}\t{ident},{tfidf}".format(ident=ident,
                                               word=word,
                                               tfidf=tfidf))


"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
