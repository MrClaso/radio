# SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MAX9744 20W class D amplifier I2C control.
# This show how to set the volume of the amplifier.
import board
import busio
import time
import adafruit_max9744

import mpd

# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize amplifier.
amp = adafruit_max9744.MAX9744(i2c)
# Optionally you can specify a different addres if you override the AD1, AD2
# pins to change the address.
# amp = adafruit_max9744.MAX9744(i2c, address=0x49)

client = mpd.MPDClient()
client.connect("localhost", 6600)
playlist="/home/pi/radio/Stationer/SR.m3u"

client.add("https://sverigesradio.se/topsy/direkt/701-hi.mp3")

# Setting the volume is as easy as writing to the volume property (note
# you cannot read the property so keep track of volume in your own code if
# you need it).
amp.volume = 34  # Volume is a value from 0 to 63 where 0 is muted/off and
# 63 is maximum volume.


print(client.playlistinfo())

print(client.mpd_version)

print("Spela P4 Stockholm")
client.play()
time.sleep(6)


# In addition you can call a function to instruct the amp to move up or down
# a single volume level.  This is handy if you just have up/down buttons in
# your project for volume:
print("Sänk volymen 6 enheter")
amp.volume_down()  # Decrease volume by one level.
amp.volume_down()  # Decrease volume by one level.
amp.volume_down()  # Decrease volume by one level.
amp.volume_down()  # Decrease volume by one level.
amp.volume_down()  # Decrease volume by one level.
amp.volume_down()  # Decrease volume by one level.
time.sleep(6)

print("Pausa")
client.pause()
time.sleep(6)

print("Fortsätt")
client.pause()
time.sleep(6)

print("Höj volymen 10 enheter")
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
amp.volume_up()  # Increase volume by one level.
time.sleep(6)

print("Sätt volymen till 25")
amp.volume = 25
time.sleep(6)

print("Sätt volymen till 48")
amp.volume = 48
time.sleep(6)

print("Stäng av")
client.stop()

