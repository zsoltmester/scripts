#!/bin/sh

date=$(date)

result=$(/usr/local/bin//speedtest-cli --simple)
ping=$(echo "$result" | grep Ping | cut -d ":" -f 2 | xargs)
download=$(echo "$result" | grep Download | cut -d ":" -f 2 | xargs)
upload=$(echo "$result" | grep Upload | cut -d ":" -f 2 | xargs)

echo "$date\t$ping\t$download\t$upload" >> /home/zsmester/log/network-speed.log
