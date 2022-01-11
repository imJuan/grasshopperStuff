from flask import Flask
import ghhops_server as hs
import rhino3dm
import cv2 
import mediapipe as mp
import handTrackingModule as htm
import math

# Flask as middleware
app = Flask(__name__)
hops = hs.Hops(app)

# Handtracking setup
cap = cv2.VideoCapture(0)
detector = htm.handDetector(maxHands=1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# HandTest
@hops.component(
    "/handtest",
    name="HandTest",
    description="Distance between two hand landmarks (https://google.github.io/mediapipe/solutions/hands.html#max_num_hands)",
    inputs=[
        hs.HopsInteger("Landmark1", "Lm1", "First landmark index"),
        hs.HopsInteger("Landmark2", "Lm2", "Second landmark index")
    ],
    outputs=[
        hs.HopsNumber("Distance", "D", "Distance")
    ]
)
def handtest(lm1, lm2):
	success, img = cap.read()

	img = detector.findHands(img)
	lmList = detector.findPositions(img)

	d = -1
	if len(lmList) != 0:
		p1 = lmList[lm1]
		p2 = lmList[lm2]
		d = math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) + ((p1[2]-p2[2])**2) )

	return d


if __name__ == "__main__":
    app.run(debug=False)
 