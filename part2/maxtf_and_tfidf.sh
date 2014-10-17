#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
INPUT="/users/nrieb/nytimes/df"
OUTPUT="/users/nrieb/nytimes/tfidf"

echo "======================STARTING MAXTF - TFIDF MAP REDUCE==================="
$HADOOP_HOME/bin/hadoop dfs -rmr $OUTPUT
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-*streaming*.jar \
    -file maxtf_mapper.py \
    -mapper maxtf_mapper.py \
    -file maxtf_reducer.py \
    -reducer maxtf_reducer.py \
    -input $INPUT/* \
    -output $OUTPUT
