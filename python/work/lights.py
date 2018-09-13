import time
import sys

from neopixel import *

# LED strip configuration:
# LED strip configuration:
LED_COUNT   = 20      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
SUN_LED_START = 15
SUN_LED_COUNT = 5

LED_RED	= sys.argv[1]
LED_GREEN = sys.argv[2]
LED_BLUE = sys.argv[3]
LED_COLOR = LED_RED + ',' + LED_GREEN + ',' + LED_BLUE
print LED_RED + ',' + LED_GREEN + ',' + LED_BLUE

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

def colorAll(strip,LED_RED,LED_GREEN,LED_BLUE):
	
        for i in range(strip.numPixels()):
            strip.setPixelColorRGB(i, int(LED_RED),int(LED_GREEN),int(LED_BLUE))
        strip.show()
		
colorAll(strip,LED_RED,LED_GREEN,LED_BLUE)