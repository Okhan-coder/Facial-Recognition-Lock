from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os


imagePaths = list(paths.list_images('/home/pi/Facial-Recognition-Lock/Dataset'))
KnownData=[]
KnownPeople=[]
for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]
	# load the input image and convert it from BGR (OpenCV ordering)
	# to dlib ordering (RGB)
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(rgb,
		model="HoG")
	encodings = face_recognition.face_encodings(rgb, boxes)
	for encoding in encodings:
		# add each encoding + name to our set of known names and
		# encodings
		KnownData.append(encoding)
		KnownPeople.append(name)
print("[INFO] serializing encodings...")
data = {"encodings": KnownData, "names": KnownPeople}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()