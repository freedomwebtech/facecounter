import numpy as np
import cv2
import cvlib as cv


cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    flipped = cv2.flip(frame, flipCode = -1)
    frame1 = cv2.resize(flipped, (640, 480))
    faces, conf = cv.detect_face(frame1)
#    print (faces)
    list=[]
    for id,face in enumerate (faces):
        
        (x,y) = (face[0]-28,face[1]-28)
        (x1,y1) = (face[2]+28,face[3]+28)
        cv2.rectangle(frame1, (x,y), (x1,y1), (0,255,0), 2)
        list.append([id,faces])
    a=len(list)
    cv2.putText(frame1,"counter:"+str(a),(20,50),0,2,(250,0,150),3)
    cv2.imshow('frame',frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()