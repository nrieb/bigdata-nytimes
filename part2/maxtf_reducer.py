#!/usr/bin/env python
"""Takes id \t word,tf,df gives back word,id \t ntf_idf"""

from __future__ import print_function, division
import sys
import json
from math import log
import logging

DOC_COUNT = 40558.0

#   is_int :: String -> Bool
def is_int(string):
    """Determines if string is formed like int"""
    try:
        int(string)
    except:
        return False
    return True

def idf(doc_freq):
    """Calculate inverse document frequency"""
    return log(DOC_COUNT/doc_freq, 10)

def max_tf_norm(tf, max_tf):
    """Maximum tf normalization"""
    return 0.4 + (1-0.4) * tf / max_tf


#   main :: IO ()
def main():
    """main processor"""
    prev_ident = None
    storage = []
    format_str = "{word},{id}\t{ntf_idf}"
    max_tf = 0
    for line in sys.stdin:
        line = line.strip()
        ident, value = line.split('\t', 1)
        word, term_freq, doc_freq = value.split(",", 2)
        
        if prev_ident and prev_ident != ident:
            for term, tf, df in storage:
                ntf_idf = max_tf_norm(tf, max_tf) * idf(df)
                print(format_str.format(word=term,
                                        id=prev_ident,
                                        ntf_idf=ntf_idf))
            max_tf = 0
            storage = []

        if is_int(term_freq):
            if int(term_freq) > max_tf:
                max_tf = int(term_freq)
            storage.append((word, int(term_freq), int(doc_freq)))
            prev_ident = ident

    if max_tf:
        for term, tf, df in storage:
            ntf_idf = max_tf_norm(tf, max_tf) * idf(df)
            print(format_str.format(word=term,
                                    id=prev_ident,
                                    ntf_idf=ntf_idf))

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
