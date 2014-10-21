#!/bin/bash

FILE_NAME="clusters.txt"

for i in {0..23}
do
    echo "================== LABEL $i ============================="
    #num_docs for cluster $i
    cat $FILE_NAME | cut -d "," -f 1,2 | sort | uniq | ack ",$i$"| sort -u | wc -l
    #wordid,docs_with_wordid for cluster $i
    cat $FILE_NAME | cut -d "," -f 2,3 | sort | ack "^$i," | cut -d "," -f 2 | uniq -c | sort -r -k1,1n | tail -n 20 | ack "(\d+) (.+)" --output '$2,$1'
done
