import time
import board
import busio
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

time.sleep(2)

for i in range(10, -1, -1):
   # print(i)
    print('{num:06d}'.format(num=i))
   # print('{num:02d}'.format(num=i))
    display.fill(0)
    display.print(':')
   # display.print(i)
    display.print('{num:06d}'.format(num=i))
    time.sleep(1)
