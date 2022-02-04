from pyfirmata import Arduino
from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

board = Arduino('/dev/cu.usbmodem101')
pin13 = board.get_pin('d:13:o')

@hops.component(
    "/led",
    name="Led",
    inputs=[
        hs.HopsNumber("A")
    ]
)
def led(A):
    pin13.write(A)

if __name__ == "__main__":
    app.run()
