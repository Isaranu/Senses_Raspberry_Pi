import requests
import time

def senddata(_userid,_devkey,_slotnum,_data):

    #Input data
        userid = _userid
        devkey = _devkey
        slotnum = _slotnum
        data = _data

        #Merge data
        payload = userid + '/' + devkey + '/' + slotnum + '/' + str(data)

        #Send to Sensesiot.com
        r = requests.get('http://www.sensesiot.com:4000/send/'+payload)
        response = r.text
        
        #Response from server
        return response

def getversion():
    #Get version of sensesiot.py
        return '1.0'    
