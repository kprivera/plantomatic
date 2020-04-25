#!/usr/bin/python

#SwitchDoc Labs May 2016
#
# reads all four channels from the Grove4Ch16BitADC Board in single ended mode
# also reads raw values
#


import time, signal, sys, json
sys.path.append('/home/pi/plants/SDL_Adafruit_ADS1x15')

import SDL_Adafruit_ADS1x15 

def signal_handler(signal, frame):
        print( 'You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ADS1115 = 0x01	# 16-bit ADC

# Select the gain
# gain = 6144  # +/- 6.144V
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Select the sample rate
# sps = 8    # 8 samples per second
# sps = 16   # 16 samples per second
# sps = 32   # 32 samples per second
# sps = 64   # 64 samples per second
# sps = 128  # 128 samples per second
sps = 250  # 250 samples per second
# sps = 475  # 475 samples per second
# sps = 860  # 860 samples per second

# Initialise the ADC using the default mode (use default I2C address)
adc = SDL_Adafruit_ADS1x15.ADS1x15(ic=ADS1115)

moist = {
	"c0": adc.readADCSingleEnded(0, gain, sps) / 1000,
	"c1": adc.readADCSingleEnded(1, gain, sps) / 1000,
	"c2": adc.readADCSingleEnded(2, gain, sps) / 1000,
	"c3": adc.readADCSingleEnded(3, gain, sps) / 1000
}

print(json.dumps(moist))
