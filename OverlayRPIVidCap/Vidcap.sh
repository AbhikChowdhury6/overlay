#!/bin/bash
t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
productName=$2
sensorName=$1
port=$3
name=/home/pi/$path$productName-$sensorName-$t-.h264
echo $name
raspivid -t 36000000 -ih -fps 10 -o $name &
