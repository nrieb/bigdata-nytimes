#! /bin/bash

HADOOP_HOME="/usr/local/hadoop"
DATA_PATH="~/bigdata-nytimes/part1"
DFS_HOME="/users/nrieb/nytimes"

$HADOOP_HOME/bin/hadoop dfs -copyFromLocal $DATA_PATH/articles.json $DFS_HOME/orig/articles.json
