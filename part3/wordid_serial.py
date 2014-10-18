#!/usr/bin/env python
"""word \t docid,tfidf"""
from __future__ import print_function
import sys

def main():
    """main function"""
    prev_word = None
    word_id = 0
    values = []
    for line in sys.stdin:
        line = line.strip()
        word, value = line.split("\t", 1)
        if prev_word and prev_word != word:
            for ident, tfidf in values:
                print("{ident},{word},{word_id},{tfidf}".format(ident=ident,
                                                                word=prev_word,
                                                                word_id=hex(word_id),
                                                                tfidf=tfidf))
            word_id += 1
            values = []

        values.append(value.split(",", 1))
        prev_word = word
    if prev_word and len(values):
        for ident, tfidf in values:
            print("{ident},{word},{word_id},{tfidf}".format(ident=ident,
                                                            word=prev_word,
                                                            word_id=hex(word_id),
                                                            tfidf=tfidf))


"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
