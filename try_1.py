import cv2 
# kütüphaneyi import ettik

face_cascade = cv2.CascadeClassifier(
    r"classifier\haarcascade_frontalface_alt.xml")
# eğitmek istediğimiz model

img = cv2.imread(r"veri1.jpg")
# üzerinde çalışılacak foto
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# renk ayari fln

faces = face_cascade.detectMultiScale(gray,1.1,4)
# keskinleştirme ayarı fln

for(c,y,w,h) in faces :
    cv2.rectangle(img , (x,y),(x+w , y+h),(0,255,0),3)
# for ile data işleri

cv2.imshow(img,"img")
# fotoyu açtık

cv2.waitKey(0)