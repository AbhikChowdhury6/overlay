#!/bin/bash
raspivid -t 0 -n -w 1280 -h 720 -hf -ih -fl -fps 20 -o - | tee >test1.h264 | nc -k -l 2322
