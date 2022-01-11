import cv2
import mediapipe as mp

class handDetector():
	def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackCon=0.5):
		self.mode = mode
		self.maxHands = maxHands
		self.model_complexity = model_complexity
		self.detectionCon = detectionCon
		self.trackCon = trackCon

		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils

	# Get hands in view
	def findHands(self, img, draw=False):
		img.flags.writeable = False
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)
		img.flags.writeable = True

		# Hand is in view
		if self.results.multi_hand_landmarks:
			# Cycle through all hands in view
			for handLandmarks in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)

		return img

	# Landmarks of specified hand
	def findPositions(self, img, handNo=0, draw=False):
		landmarkList = []

		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				h, w, c = img.shape
				cx, cy = int(lm.x * w), int(lm.y * h)

				landmarkList.append([id,cx,cy])

				if draw:
					cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)

		return landmarkList