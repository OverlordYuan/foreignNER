#!/bin/sh
source venv/bin/activate
for var in 5001 5002 5003 5004 5005 5006 5007 5008
do
    nohup gunicorn -w 4 -b 0.0.0.0:$var spacyNER_gunicorn:app --timeout 200 >> $var.out &
done
