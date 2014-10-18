#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
INPUT="/users/nrieb/nytimes/tfidf"
OUTPUT="/users/nrieb/nytimes/wordid"

echo "======================STARTING MAXTF - TFIDF MAP REDUCE==================="
$HADOOP_HOME/bin/hadoop dfs -rmr $OUTPUT
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-*streaming*.jar \
    -file wordid_mapper.py \
    -mapper wordid_mapper.py \
    -file wordid_reducer.py \
    -reducer wordid_reducer.py \
    -input $INPUT/* \
    -output $OUTPUT

$HADOOP_HOME/bin/hadoop fs -get $OUTPUT .
