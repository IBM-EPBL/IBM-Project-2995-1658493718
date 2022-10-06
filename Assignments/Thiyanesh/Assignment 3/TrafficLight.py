from gpiozero import TrafficLights    
from time import sleep    
lights = TrafficLights(25, 8, 7)     
while True:    
    lights.green.on()    
    sleep(5)    
    lights.amber.on()    
    sleep(1)    
    lights.red.on()    
    sleep(5)      
