#!/bin/sh

ls /etc/ | wc -l | awk '{print $1}'  >/tmp/pyhk/run.log

sleep 1; echo "10,20" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >/tmp/pyhk/run.csv


sleep 1; echo "20,30" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv


sleep 1; echo "30,40" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv


sleep 1; echo "40,50" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv


sleep 1; echo "50,60" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv


sleep 1; echo "60,70" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv


sleep 1; echo "70,80" | awk '{x="'"`date +%s`"'"; printf "%s,%s\n",x,$0 }' >>/tmp/pyhk/run.csv
