#!/bin/bash
devices=`adb devices|grep 'device'|awk 'NR==1 {next}  {print $1}'`
for device in $devices;do
}
done

