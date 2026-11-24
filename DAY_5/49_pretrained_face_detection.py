# 49 Face detection using pretrained OpenCV Haar cascade (not identity recognition)
import cv2
im=cv2.imread("face_photo.jpg")
if im is None:raise FileNotFoundError("Add face_photo.jpg")
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
faces=c.detectMultiScale(gray,1.1,5)
for x,y,w,h in faces:cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
print("Faces detected:",len(faces));cv2.imshow("Face detection",im);cv2.waitKey(0);cv2.destroyAllWindows()