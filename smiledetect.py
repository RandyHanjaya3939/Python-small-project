import cv2

TrainFace = cv2.CascadeClassifier(f'{cv2.haarcascades}haarcascade_frontalface_default.xml')
TrainSmile = cv2.CascadeClassifier(f'{cv2.haarcascades}haarcascade_smile.xml')

vid = cv2.VideoCapture(2)

while True:
    (success_test , frame) = vid.read()

    if success_test:
        grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    coorFace = TrainFace.detectMultiScale(grayvid)

    for (x,y,w,h) in coorFace:
        cv2.rectangle(frame , (x,y) , (x+w, y+h) , (0,255,0) , 2)

        #hanya mencari smile didalam face yang terdeteksi
        coorSmile = TrainSmile.detectMultiScale(grayvid, scaleFactor = 1.7, minNeighbors = 20)
        for(a,b,c,d) in coorSmile:
            cv2.rectangle(frame , (a,b) , (a+c, b+d) , (0,0,255) , 2)

    cv2.imshow('SmileDetect', frame)
    Key = cv2.waitKey(1)

    if Key == 81 or Key == 113:
        break

vid.release()