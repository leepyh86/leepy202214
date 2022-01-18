#!/bin/bash gird脚本分发给不同的节点执行
for i in `adb devices|grep 'device'|awk 'NR==1 {next}  {print $1}'`
do
  echo $i
  udid=$i py test_a.py &
done