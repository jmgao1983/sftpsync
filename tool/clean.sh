#!/bin/bash
# usage: copy following line into file: /etc/cron.d/xxx_clean
# 5 6 2 * * root /bin/bash /home/jmgao/sftpsync/tool/clean.sh > /dev/null 2>&1

set -o nounset
set -o errexit
#set -x

FilesToClean=$(find /home/jmgao/sftpsync/data -name "cmm*" -mtime +180)
LogTime=$(date +"%Y-%m-%d %H:%M:%S")
echo -e "$LogTime" + "{\n $FilesToClean" + "\n}to be removed" >> /home/jmgao/sftpsync/log/cron.log

for F in $FilesToClean; do rm -f $F; done;
