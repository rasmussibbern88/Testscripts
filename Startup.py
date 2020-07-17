#Init script

from IOPi import IOPi
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)# Pin layout setting
GPIO.setup(17, GPIO.OUT)# pin output or input
GPIO.output(17, GPIO.HIGH)#Tænd for blæser, skal måske være LOW?

GPIO.setup(27, GPIO.OUT)# pin output or input
GPIO.output(27, GPIO.HIGH)

GPIO.setup(22, GPIO.OUT)# pin output or input
GPIO.output(22, GPIO.HIGH)

GPIO.setup(10, GPIO.OUT)# pin output or input
GPIO.output(10, GPIO.HIGH)

GPIO.setup(9, GPIO.OUT)# pin output or input
GPIO.output(9, GPIO.HIGH)


R
GPIO.setup(14, GPIO.OUT)# pin output or input
GPIO.output(14, GPIO.HIGH)
G
GPIO.setup(15, GPIO.OUT)# pin output or input
GPIO.output(15, GPIO.HIGH)
B
GPIO.setup(18, GPIO.OUT)# pin output or input
GPIO.output(18, GPIO.HIGH)


#C
# GPIO.output(9, GPIO.LOW)
# GPIO.output(22, GPIO.LOW)

# GPIO.output(9, GPIO.HIGH)
# GPIO.output(22, GPIO.HIGH)

#CC
# GPIO.output(10, GPIO.LOW)
# GPIO.output(27, GPIO.LOW)
#
# GPIO.output(10, GPIO.HIGH)
# GPIO.output(27, GPIO.HIGH)


#GPIO.setup(port_or_pin, GPIO.OUT, initial=1)

bus = IOPi(0x20)# Tilføj flere busser her
bus2 = IOPi(0x21)

bus.set_port_direction(0, 0x00)
time.sleep(1.5)
bus.write_port(0, 0xFF)
time.sleep(1.5)
bus.set_port_direction(1, 0x00)
time.sleep(1.5)
bus.write_port(1, 0xFF)

bus2.set_port_direction(0, 0x00)
time.sleep(1.5)
bus2.write_port(0, 0xFF)
time.sleep(1.5)
bus2.set_port_direction(1, 0x00)
time.sleep(1.5)
bus2.write_port(1, 0xFF)


#bus.write_pin(1, 1) pin 1-16 and 1 for off or 0 for on

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
