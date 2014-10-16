#!/usr/bin/env python
"""id \t word,tf,df from word,id \t tf,df"""
from __future__ import print_function
import sys

def main():
    """main function"""
    for line in sys.stdin:
        line = line.strip()
        key, tf_df = line.split("\t", 1)
        word, ident = key.split(",", 1)
        print("{ident}\t{word},{tf_df}".format(ident=ident,
                                               word=word,
                                               tf_df=tf_df))


"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
