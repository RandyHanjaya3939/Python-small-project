import cv2

classifier = cv2.CascadeClassifier('car_haarcascade.xml')

imgcv = cv2.imread('car.jpg')

scale_percent = 25 # percent of original size
width = int(imgcv.shape[1] * scale_percent / 100)
height = int(imgcv.shape[0] * scale_percent / 100)
dim = (width, height)

resizeimg = cv2.resize(imgcv,dim)
GrayImage = cv2.cvtColor(resizeimg, cv2.COLOR_BGR2GRAY)

coor = classifier.detectMultiScale(GrayImage,minNeighbors = 1)
for (x,y,w,h) in coor:
    cv2.rectangle(resizeimg, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Traffic Detection", resizeimg)
cv2.waitKey()