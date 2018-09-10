#!/bin/bash
t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
productName=$2
sensorName=$1
port=$3
path="/media/chowderhat/18CE0051CE002998/"
name=$path$productName-$sensorName-$t-.h264
echo $name
ffmpeg -i /dev/video1 -c:v libx264 -preset ultrafast -crf 0 $name
