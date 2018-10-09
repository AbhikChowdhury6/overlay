#!/bin/bash
port=$1
raspivid -t 0 -n -w 1920 -h 1080 -ih -fl -fps 4 -o - | nc -k -q -1 -l $port  &
