import time
import grovepi
import os
import Image

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        # Sense motion, usually human, within the target range
        if grovepi.digitalRead(pir_sensor):
            print 'Motion Detected'
            os.system ("cp /home/pi/Pictures/image2/image2.png /var/www/html/image.png")
            time.sleep(5)
            os.system ("cp /home/pi/Pictures/image1/image1.png /var/www/html/image.png")
        else:
            print '-'

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.5)

    except IOError:
        print "Error"
