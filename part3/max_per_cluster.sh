#!/bin/bash

FILE_NAME="clusters.txt"

for i in {0..23}
do
    echo "================== LABEL $i ============================="
    cat $FILE_NAME | cut -d "," -f 2,3,4 | sort | ack "^$i" | cut -d "," -f 2,3 | sort -t"," -k2,2n | uniq | tail -n 20
done
