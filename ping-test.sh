#!/bin/dash

date=$(date)

result_router=$(sudo ping 192.168.0.1 -c 10 -n -q | tail -n 1 | cut -d '/' -f 5)
result_google=$(sudo ping google.com -c 10 -n -q | tail -n 1 | cut -d '/' -f 5)

echo "$date\t$result_router\t$result_google" >> /home/zsmester/log/ping.log

