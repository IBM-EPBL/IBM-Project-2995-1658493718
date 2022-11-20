import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "liv8qw"
deviceType = "sthiyanesh"
deviceId = "sthiyanesh"
authMethod = "token"
authToken = "sthiyanesh"
valve1="Opened";
valve2="Opened";
valve3="Opened";
valve4="Closed";
valve5="Opened";
# Initialize GPIO

def myCommandCallback(cmd):
    global valve1,valve2,valve3,valve4,valve5;
    #print("Command received: %s" % cmd.data['valve1'])
    ValveNumber=cmd.data['Valve']
    ValveState=cmd.data['State']
    if(((ValveNumber==1)|(ValveNumber=="1"))):
        valve1=ValveState
        print(valve1)
    if((ValveNumber==2)|(ValveNumber=="2")):
        valve2=ValveState
    if((ValveNumber==3)|(ValveNumber=="3")):
        valve3=ValveState
    if((ValveNumber==4)|(ValveNumber=="4")):
        valve4=ValveState
    if((ValveNumber==5)|(ValveNumber=="5")):
        valve5=ValveState
    print("Valve "+str(ValveNumber)+" is "+ValveState)

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        Sensor1= random.randint(0,500)
        Sensor2= random.randint(0,500)
        Sensor3= random.randint(0,500)
        Sensor4= random.randint(0,500)
        Sensor5= random.randint(0,500)
        data = {"SensorData":{ 'Sensor1' : Sensor1, 'Sensor2': Sensor2 ,'Sensor3': Sensor3,"Sensor4":Sensor4,"Sensor5":Sensor5},"ValveData":{ "Valve1" : { "Valve": 1, "State": valve1 },"Valve2" : { "Valve": 2, "State": valve2 },"Valve3" : { "Valve": 3, "State": valve3 },'Valve4' : { "Valve": 4, "State": valve4 },'Valve5' : { "Valve": 5, "State": valve5 } } }
        #print data
        def myOnPublishCallback():
            print ("Published ",data, "to pyIBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()