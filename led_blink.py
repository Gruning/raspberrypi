import RPi.GPIO as GPIO
import time
#pin dedinitions 
pwmPin = 18
ledPin = 23
butPin = 17

duty = 75

#setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(butPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
