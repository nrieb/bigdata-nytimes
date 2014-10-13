#!/usr/bin/env python
"""Takes [(term,url)] and gives back [(term,(url,tf-idf))]"""

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

#   multiset_length :: [(String, Int)] -> Int
def multiset_length(multiset):
    length = 0
    for (_, count) in 

#   main :: IO ()
def main():
    """main processor"""
    prev_url = None
    prev_term = None
    count = 0
    multiset = []
    terms = []
    for line in sys.stdin:
        term, url = line.split('\t', 1)
        if (prev_term and prev_term != term) or (prev_url and prev_url != term):
            multiset.append((url, count))
            count = 0
            prev_url = url

        if prev_term and prev_term != term:
            terms.append((prev_term, multiset))
            prev_term = term
            multiset = []
            prev_url = None

    


'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
