#!/bin/bash

echo "start predict server"
nohup python predict_server.py "$1" "$2" "$3"> /tmp/predict_server.log 2>&1 &
sleep 1
