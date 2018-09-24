#bash upload.sh chowder test_data pass 192.168.1.xxx
IP=$4
user=$1
path=$2
pass=$3

#pkill python
for filename in *.csv; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    echo sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done

pkill arecord
for filename in *.wav; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    echo sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done

pkill raspivid
for filename in *.h264; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    echo sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done
