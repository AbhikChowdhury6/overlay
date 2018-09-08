#!/bin/bash
t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
productName=$2
sensorName=$1
name=$productName-$sensorName-$t-.wav
echo $name
arecord --device=hw:1,0 --format S16_LE --rate 44100 -c2 $name
