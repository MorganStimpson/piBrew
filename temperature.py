# Morgan Stimpson
# Borrowed from
# https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9

# temp sensor; DS18B20 -- water proof temperature sensor
# plug in points;   RED         -> 3.3V                     |   pin: 1
#                   Blue/Black  -> Ground                   |   pin: 6
#                   Yellow      -> Pull-Up Resistor/pin 4   |   pin: 5 (gpio 3)

import os
import glob
import time
# from ISStreamer.Streamer import Streamer # this I am unsure on -- remember pip uninstall ISStreamer if undeeded

# streamer = Streamer(bucket_name="Temperature Stream", bucket_key="piot_temp_stream031815", access_key="PUT_YOUR_ACCESS_KEY_HERE") # replace this with the proper access key.
# if the access key is correct than it should run correctly
# the way to get the correct value is 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

while True:
    temp_c = read_temp()
    temp_f = temp_c * 9.0 / 5.0 + 32.0

    print("temperature F:", temp_f)

    # streamer.log("temperature (C)", temp_c)
    # streamer.log("temperature (F)", temp_f)
    time.sleep(1)