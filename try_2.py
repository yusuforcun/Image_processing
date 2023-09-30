import numpy as np
import cv2

vid = cv2.VideoCapture(0)

yuz_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while(True):
    ret,frame = vid.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = yuz_cas.detectMultiScale(gray , 1.3 , 5 )
    print(faces)
    
    for (x, y, w, h) in faces:
            # Yüz tespit edildiğinde, yüzün orta noktasını hesaplayın
        center_x = x + w // 2
        center_y = y + h // 2
    
        if 200 < center_x < 440 and 100 < center_y < 340:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (96, 170, 0), 3)

# TÜM YÜZLER İÇİN 
    # for(x,y,w,h) in faces:  
        # cv2.rectangle(frame,(x, y),(x+w , y + h ),(80,250,0),3)
        
    cv2.imshow("title",frame)
    cv2.imwrite("selfie.jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break  
    
vid.release()
cv2.destroyAllWindows()