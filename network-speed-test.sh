#!/bin/sh

date >> /home/zsmester/log/network-speed.log
speedtest-cli >> /home/zsmester/log/network-speed.log
echo "" >> /home/zsmester/log/network-speed.log
