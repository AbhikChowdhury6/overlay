#!/bin/bash
t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
productName=$2
sensorName=$1
name=$productName-$sensorName-$t-.h264
echo $name
raspivid -t 0 -n -w 1920 -h 1080 -hf -ih -fl -fps 10 -o - | tee >$name #| nc -k -l 2222
