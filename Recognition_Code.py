from imutils import paths
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import face_recognition
import argparse
import pickle
import cv2
import os
import time
import numpy
# Load the cascade and facial recognition data
data=pickle.loads(open("encodings.pickle","rb").read())
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video  
vs= VideoStream(usePiCamera=True).start()
writer=0
time.sleep(2.0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
fps=FPS().start()
while True:
    # Read the frame
    snapshot=vs.read()
    snapshot=imutils.resize(snapshot,width=500)
    # Convert to grayscale
    gray = cv2.cvtColor(snapshot,cv2.COLOR_BGR2GRAY )
    rgb = cv2.cvtColor(snapshot,cv2.COLOR_BGR2RGB )
    # Detect the faces
    facebox = face_cascade.detectMultiScale(gray, 1.1, 4,minSize=(30,30))
    # Draw the rectangle around each face
        
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in facebox]
   
    print(boxes)
    # compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(rgb, boxes)
    print(boxes)
    names = []
    
    for encoding in encodings:
     print("Recognize step")
     # attempt to match each face in the input image to our known
     # encodings
     matches = face_recognition.compare_faces(data["encodings"],encoding)
     name = "Unknown"
        # check to see if we have found a match
     if True in matches:
            # find the indexes of all matched faces then initialize
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
        # update the list of names
    try:
        names.append(name)
    except:
        pass
    # loop over the facial embeddings
    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # draw the predicted face name on the image
        cv2.rectangle(snapshot, (left, top), (right, bottom),(0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(snapshot, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 255, 0), 2)
    # display the image to our screen
    cv2.imshow("Frame", snapshot)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    # update the FPS counter
    fps.update()
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
