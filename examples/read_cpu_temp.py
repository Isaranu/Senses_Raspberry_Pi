from sensesiot import *

#Get version of sensesiot.py
version = getversion()
print(version)

#Senses IoT account userid : https://www.sensesiot.com/accountinfo
userid = 'your-userid-number'

#Senses IoT registered iot device key (My IoT garage) : https://www.sensesiot.com/myiotgarage
key = 'your-registered-device-key'

#Your desired sending data
slotnum = 'your-slot-number-of-data'

while True:
  #Read CPU temperature of RPi
  cpu_temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
  print('CPU temperature : ' ,cpu_temp, ' celcius')
  
  #Send data to Senses IoT platform.
  res = senddata(userid, key, slotnum, cpu_temp)

  #Response
  print(res)
  
  #Wait for 5 looping.
  time.sleep(5)
