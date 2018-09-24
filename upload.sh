#bash upload.sh chowder test_data 192.168.1.xxx
IP=$4
user=$1
path=$2
pass=$3

for filename in *.csv; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done

for filename in *.wav; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done

for filename in *.h264; do
    echo $filename
    arrIN=(${filename//-/ })
    productName=${arrIN[0]}
    echo ${arrIN[0]}
    sensorName=${arrIN[1]}
    echo ${arrIN[1]}
    sshpass -p $pass scp $filename $user@$IP:$path/$productName/$sensorName
    rm $filename
done
