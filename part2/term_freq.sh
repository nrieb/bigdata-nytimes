#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
SCRIPT_PATH="~/bigdata-nytimes/part2"

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-*streaming*.jar \
    -file $SCRIPT_PATH/porter2.py
    -file $SCRIPT_PATH/tf_mapper.py \
    -mapper $SCRIPT_PATH/tf_mapper.py \
    -file $SCRIPT_PATH/tf_reducer.py \
    -reducer $SCRIPT_PATH/tf_reducer.py \
    -input /users/nrieb/nytimes/orig/* \
    -output /users/nrieb/nytimes/tf
