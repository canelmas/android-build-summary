#!/bin/sh

for i in $*;
do
    params=" $params $d$i"
done

python ~/jenkins/helpers/summarize.py $params