from unicodedata import name
from flask import Flask
import ghhops_server as hs
from rhino3dm import *

import cv2
import mediapipe as mp

app = Flask(__name__)
hops = hs.Hops(app)


# Could later create component to open and close video capture
mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)

@hops.component(
	"/facemesh",
	name="Face Mesh",
	description="Get face mesh from webcam... points for now. will do mesh later",
	outputs=[
		hs.HopsPoint("P", "Points", "Mesh points from landmarks")
	]
)
def facemesh():
	points = []

	with mp_face_mesh.FaceMesh(
		max_num_faces = 1,
		refine_landmarks=True,
		min_detection_confidence=0.5) as face_mesh:
		success, image = cap.read()

		if not success:
			return
			
		image.flags.writeable = False
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		results = face_mesh.process(image)

		h, w, c = image.shape

		if (results.multi_face_landmarks):
			for face in results.multi_face_landmarks:
				for lm in face.landmark:
					points.append(Point3d(lm.x*w, lm.y*h, lm.z*h))
	return points


if __name__ == "__main__":
	app.run()