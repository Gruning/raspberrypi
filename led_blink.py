import RPi.GPIO as GPIO
import time
#pin dedinitions 
pwmPin = 18
ledPin = 23
butPin = 17

duty = 75

#setup GPIO
GPIO.setmode(GPIO.BCM)