#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
INPUT="/users/nrieb/nytimes/tf"
OUTPUT="/users/nrieb/nytimes/df"

echo "======================STARTING DOC FREQ MAP REDUCE==================="
$HADOOP_HOME/bin/hadoop dfs -rm $OUTPUT/*
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-*streaming*.jar \
    -file df_mapper.py \
    -mapper df_mapper.py \
    -file df_reducer.py \
    -reducer df_reducer.py \
    -input $INPUT/* \
    -output $OUTPUT
