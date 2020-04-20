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
  
  data = randrandrange(15,20) #replace-your-data-here
  
  #Send data to Senses IoT platform.
  res = send(userid, key, slotnum, data)

  #Response
  print(res)
  
  #Wait for 5 looping.
  time.sleep(5)
