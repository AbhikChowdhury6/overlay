#!/bin/bash
t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
productName=$2
sensorName=$1
name=/home/pi/$productName-$sensorName-$t-.wav
echo $name
arecord -D plughw:1 -c2 -r 48000 -f S32_LE -t wav -V stereo -v $name &
