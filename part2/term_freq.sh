#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
SCRIPT_PATH="~/bigdata-nytimes/part2"

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-*streaming*.jar \
    -file porter2.py \
    -file tf_mapper.py \
    -mapper tf_mapper.py \
    -file tf_reducer.py \
    -reducer tf_reducer.py \
    -input /users/nrieb/nytimes/orig/* \
    -output /users/nrieb/nytimes/tf
