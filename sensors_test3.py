##Using Python 2.7.3

##Import the GPIO library
import RPi.GPIO as gpio
##Import the time library
import time
##Import the local sensors library
import sensors

##Test 3: check that the servo motor is correctly wired and functional
##Expected result: Servo motor moves to center, left ~30 degrees, right ~30 degrees, back to center
sensors.front_pan()

##Troubleshooting: