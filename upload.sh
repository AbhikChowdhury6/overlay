#!/bin/bash

#bash upload.sh chowder test_data pass 192.168.1.xxx
IP=$4
user=$1
path=$2
pass=$3

#pkill python
for filename in *.csv; do
    [ -f "$filename" ] || break
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass ssh $user@$IP mkdir -p $path/$productName/$sensorName
    echo rsync -r $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass rsync -r -e ssh $filename $user@$IP:$path/$productName/$sensorName
done

pkill arecord
for filename in *.wav; do
    [ -f "$filename" ] || break
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass ssh $user@$IP mkdir -p $path/$productName/$sensorName
    echo rsync -r $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass rsync -r -e ssh $filename $user@$IP:$path/$productName/$sensorName
done

pkill raspivid
for filename in *.h264; do
    [ -f "$filename" ] || break
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass ssh $user@$IP mkdir -p $path/$productName/$sensorName
    echo rsync -r $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass rsync -r -e ssh $filename $user@$IP:$path/$productName/$sensorName
    #echo rm $filename
    #rm $filename
done
