import random
from sensesiot import *

#Get version of sensesiot.py
version = getversion()
print(version)

#Senses IoT account userid : https://www.sensesiot.com/accountinfo
userid = 'your-userid-number'

#Senses IoT registered iot device key (My IoT garage) : https://www.sensesiot.com/myiotgarage
key = 'your-registered-device-key'

#Your desired sending data
slotnum = '1' #Set slot data number 1

while True:
  
  data = random.randrange(15,20) #replace-your-data-here
  
  #Send data to Senses IoT platform.
  res = senddata(userid, key, slotnum, data)

  #Response
  print(res)
  
  #Wait for 5 looping.
  time.sleep(5)
