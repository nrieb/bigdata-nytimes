#!/usr/bin/env python
""" word,id\t1 output from raw json"""
from __future__ import print_function
import sys
import json
from porter2 import stem

#http://www.textfixer.com/resources/common-english-words.txt
# COMMON_ENGLISH :: [String]
COMMON_ENGLISH = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]

#   abstract_words String -> [String]
def abstract_words(abstract):
    """Get each word in the abstract, making chars lower case, removing
    non-alphabetic chars and spaces."""
    allowable_chars = unicode("abcdefghijklmnopqrstuvwxyz ")
    trimmed = "".join([char for char in abstract.lower()
                       if char in allowable_chars])
    words = []
    for word in trimmed.split(" "):
        try:
            stemmed_word = stem(word)
        except ValueError:
            stemmed_word = word
        if len(word) <= 1 or stemmed_word in COMMON_ENGLISH:
            continue
        else:
            words.append(stemmed_word)
    return words


def main():
    """main function"""
    for line in sys.stdin:
        record = json.loads(line.strip())
        if "abstract" in record and "id" in record:
            for word in abstract_words(record["abstract"]):
                print("{0},{1:x}\t1".format(word, int(record["id"], 16)))


"""-------------------------------------------------------------------------"""
if __name__ == "__main__":
    main()
