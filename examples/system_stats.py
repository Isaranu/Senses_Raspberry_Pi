#-- Before running this script, please do it on your Pi.
# $ sudo apt-get install python-pip
# $ sudo pip install psutil
#-------------------------------------------------------

import psutil
from sensesiot import *

#Get version of sensesiot.py
version = getversion()
print(version)

#Senses IoT account userid : https://www.sensesiot.com/accountinfo
userid = 'your-userid-number'

#Senses IoT registered iot device key (My IoT garage) : https://www.sensesiot.com/myiotgarage
key = 'your-registered-device-key'

#Your desired sending data
temp_slot = '0'
cpu_perc_slot = '1'

while True:
  #Read CPU temperature of RPi
  cpu_temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
  print('CPU temperature : ' ,cpu_temp, ' celcius')
  
  #Read Usage % of CPU
  cpu_perc = psutil.cpu_percent()
  print('CPU usage percent : ',cpu_perc, ' %')
  
  #Send data to Senses IoT platform.
  res = senddata(userid, key, temp_slot, cpu_temp)
  print(res)
  
  res = senddata(userid, key, cpu_perc_slot, cpu_perc)
  print(res)
  
  #Wait for 5 looping.
  time.sleep(10)
