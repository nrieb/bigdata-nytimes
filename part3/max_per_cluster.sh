#!/bin/bash

FILE_NAME="clusters.txt"
NUM_CLUSTERS=8

for i in {0..7}
do
    cat $FILE_NAME | cut -d "," -f 2,3 | sort | ack "^$i" | uniq -c | head -n 20
done
