import cv2
import os
import numpy as np
import faceRecognition as fr


#This module takes images  stored in diskand performs face recognition
test_img=cv2.imread('/Users/rohit/Desktop/FaceRecog/TestImages/test.jpg')#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)


#Uncomment belows lines when running this program first time.Since it svaes training.yml file in directory
faces,faceID=fr.labels_for_training_data('/Users/rohit/Desktop/FaceRecog/trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')
#face_recognizer=cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs

name={0:"Rohit",1:"Taylor"}#creating dictionary containing names for each label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>37):#If confidence greater than 37 then don't print predicted face text on screen
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(600,400))
cv2.imshow("Face Recog",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows





