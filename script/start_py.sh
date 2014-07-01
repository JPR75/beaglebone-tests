#!/bin/bash
cp -r /home/ubuntu/soft /home/ubuntu/ramdisk/soft
cd /home/ubuntu/ramdisk
sudo chmod a+r /home/ubuntu/ramdisk/soft/global_data.py
sudo chmod a+r /home/ubuntu/ramdisk/soft/sql_setup.py
sudo chmod a+rw /home/ubuntu/ramdisk/soft/www
sudo chmod a+rw /sys/class/leds/beaglebone::usr3/brightness
sudo python -OO /home/ubuntu/ramdisk/soft/boot.py &
