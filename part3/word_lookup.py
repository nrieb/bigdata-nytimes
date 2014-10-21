#!/usr/bin/env python
from __future__ import print_function
import sys
"""
def main():
    word_ids = sys.argv[1:]
    with open("word_id.csv", "r") as f:
        for line in f:
            line = line.strip()
            _, word, id, _ = line.split(",", 3)
            for word_id in word_ids:
                if id == word_id:
                    print word, id
"""
TOP_WORDS_FILE = "max_tf_idf.txt"
WORD_ID_FILE = "word_id.csv"

def main():
    words = []
    #word_id file sorted by word_id
    with open(WORD_ID_FILE, "r") as f:
        prev_word = None
        for line in f:
            line = line.strip()
            _, word, _, _ = line.split(",", 3)
            if prev_word != word:
                words.append(word)
            prev_word = word

    with open(TOP_WORDS_FILE) as f:
        for line in f:
            line = line.strip()
            if line[0] == "=":
                print(line)
                continue
                
            try:
                word_id, tfidf = line.split(",", 1)
            except ValueError:
                print(line,file=sys.stderr)
                raise
            word_id = int(word_id, 16)
            print("{word},{word_id:x},{tfidf}".format(word=words[word_id],
                                                      word_id=word_id,
                                                      tfidf=tfidf))
    
main()
