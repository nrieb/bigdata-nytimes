#!/usr/bin/env python
from __future__ import print_function
import sys
import numpy.numarray as na
import matplotlib.pyplot as plt

TOP_WORDS_FILE = "max_count_per_cluster.txt"
WORD_ID_FILE = "word_id.csv"

def my_plot(words, percents, group):
    plt.clf()
    plt.barh(range(len(percents)), percents, color='#000000', label="percents")
    plt.ylabel("Words")
    plt.xlabel("Percent of docs has word")
    plt.title("Group {0} - Top 20 Words".format(group))
    plt.yticks(range(len(words)), words)
    plt.savefig("group_{0}.png".format(group))
    #plt.show()

def get_id_to_words():
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
    return words

def main():
    id_to_words = get_id_to_words()
    group = None
    curr_words = []
    percents = []
    with open(TOP_WORDS_FILE) as f:
        for line in f:
            line = line.strip()
            if line[0] == "=":
                print(line)
                if group != None:
                    my_plot(curr_words, percents, group)
                    curr_words = []
                    percents = []
                    group += 1
                else:
                    group = 0
                continue
            
            if "," not in line:
                total_count = float(line)
                print(line)
                continue
                
            try:
                word_id, count = line.split(",", 1)
            except ValueError:
                print(line,file=sys.stderr)
                raise
            word_id = int(word_id, 16)
            print("{word},{percent:.3%}".format(word=id_to_words[word_id],
                                                percent=int(count)/total_count))
            curr_words.append(id_to_words[word_id])
            string = "{0:.3%}".format(int(count)/total_count)
            string = string.strip("%")
            percents.append(float(string))

    if len(curr_words) and len(percents):
        my_plot(curr_words, percents, group)
    
main()
