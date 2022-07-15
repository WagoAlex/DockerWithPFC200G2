#!/bin/sh
# Contact: Helmut.Saal@wago.com
# Version 1
# Script to copy an EC Application to the PLC
# 1. Get Host IP Adress
clear
#1 Get Host IP Adress
echo -e "\n\n"
echo -e "\e[00;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[00m"
echo -e "\e[00;33mStart configuration local.\e[00m"
echo "\e[01;36m1.\e[00m Fetching Host IP Adress....."
HOST_IP=$(ifconfig | grep inet | head -n1 | cut -d":" -f2 | cut -d" " -f1)
echo -e "Actual Host IP= \e[00;32m$HOST_IP\e[00m"
echo -e "\e[00;32mDone.\e[00m"

# 2. Connect Host via SSH - Stop eRuntime
echo -e "\e[01;36m2.\e[00m Connect Hostsystem directly via a ssh session."
echo -e "Stop eRuntime."
ssh -t -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" root@$HOST_IP << EOF
/etc/init.d/runtime stop
EOF
echo -e "\e[00;32mDone.\e[00m"
sleep 2

# 3. Copy Files
echo -e "\e[01;36m3.\e[00m Copy Application to Host."
cp /root/eRUNTIME.cfg /home/codesys_root/
cp -R /root/Application /home/codesys_root/PlcLogic/
cp -R /root/_cnc /home/codesys_root/PlcLogic/
cp -R /root/ac_persistence /home/codesys_root/PlcLogic/
cp -R /root/alarms /home/codesys_root/PlcLogic/
cp -R /root/trend /home/codesys_root/PlcLogic/
cp -R /root/visu /home/codesys_root/PlcLogic/
echo -e "\e[00;32mDone.\e[00m"

# 4. Connect Host via SSH - Start eRuntime
echo -e "\e[01;36m4.\e[00m Connect Hostsystem directly via a ssh session."
echo -e "Start eRuntime."
ssh -t -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" root@$HOST_IP << EOF
/etc/init.d/runtime start
EOF
echo -e "\e[00;32mDone.\e[00m"
echo -e "\e[00;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[00m"
echo "Finish, Application starts, Set OMS to run mode!"
echo -e "\e[00;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[00m"