#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
from PIL import Image
import pyzbar.pyzbar as pyzbar


camera = PiCamera()

while True:
    filepath = '/home/pi/Desktop/bar_test.png'
    # Take a picture
    camera.start_preview()
    sleep(5)
    camera.capture(filepath)
    camera.stop_preview()
    # Process it
    with open(filepath, 'rb') as image_file:
        image = Image.open(image_file)
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            sn = barcode.data.decode("utf-8")
            sleep(1)
            print(f'The battery SN is: {sn}')
   
