# 46 Pretrained MobileNet-SSD object detection. Requires model files and OpenCV.
import cv2
net=cv2.dnn.readNetFromCaffe("deploy.prototxt","mobilenet_iter_73000.caffemodel")
im=cv2.imread("sample_image.jpg")
if im is None:raise FileNotFoundError("Add sample_image.jpg")
blob=cv2.dnn.blobFromImage(cv2.resize(im,(300,300)),.007843,(300,300),127.5);net.setInput(blob);out=net.forward()
for i in range(out.shape[2]):
 conf=float(out[0,0,i,2])
 if conf>.5:
  x1,y1,x2,y2=(out[0,0,i,3:7]*[im.shape[1],im.shape[0],im.shape[1],im.shape[0]]).astype(int)
  cv2.rectangle(im,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("Detections",im);cv2.waitKey(0);cv2.destroyAllWindows()