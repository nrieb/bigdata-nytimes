#!/usr/bin/env python
"""Takes word \t id,tf gives back word,id \t tf, df"""

from __future__ import print_function
import sys
import json
from math import log

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
    prev_word = None
    doc_freq = 0
    storage = []
    format_str = "{word},{id}\t{tf},{df}"
    for line in sys.stdin:
        line = line.strip()
        word, value = line.split('\t', 1)

        if prev_word and prev_word != word:
            for ident, term_freq in storage:
                print(format_str.format(word=prev_word,
                                        id=ident,
                                        tf=term_freq,
                                        df=doc_freq))
            doc_freq = 0
            storage = []

        doc_freq += 1
        storage.append(value.split(",", 1))
        prev_word = word

    if doc_freq and prev_word:
        for ident, term_freq in storage:
            print(format_str.format(word=prev_word,
                                    id=ident,
                                    tf=term_freq,
                                    df=doc_freq))

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
