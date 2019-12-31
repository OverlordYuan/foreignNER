#!/bin/sh
for var in 5001 5002 5003 5004 5005 5006 5007 5008
do
    echo "shut down the poot:$var"
    for i in `ps -ef |grep "gunicorn -w 4 -b 0.0.0.0:$var" |grep -v "grep" |awk '{print $2}'`;
    do 
         echo $i;
         kill -9 $i;
    done
done
