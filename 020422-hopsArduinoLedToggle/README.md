# Setup pyfirmata

1. Install `pyfirmata` for python
2. Connect Arduino to computer and open ArduinoIDE
3. Inside of `Files/Examples` open `Firmata/StandardFirmata` file and upload to your Arduino
4. Now you can start using `pyfirmata`

Example:

```python
from pyfirmata import Arduino
import time

if __name__ == "__main__":
	board = Arduino('/dev/cu.usbmodem101')

	while True:
		board.digital[13].write(1)
		time.sleep(0.5)
		board.digital[13].write(0)
		time.sleep(0.5)
```

# Setup Grasshopper

1. Download python file and run it
2. Create Hops component in Grasshopper and set [`http://127.0.0.1:5000/led`](http://127.0.0.1:5000/led) as the Path
3. Connect a `Boolean Toggle` to the `A` input of Hops component
4. LED on Arduino could now be toggled through Grasshopper!

