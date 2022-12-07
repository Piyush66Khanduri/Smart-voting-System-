import cv2 as cv
from simple_facerec import SimpleFacerec  
def voter_identification(z):
    simp=SimpleFacerec()
    simp.load_encoding_images('images')
    fname=0
    key=0
    floca=0
    img=cv.VideoCapture(0)
    while True:
        ret,fram=img.read()
        floca,fname=simp.detect_known_faces(fram)
        for location,name in zip(floca,fname):
            y,x,y1,x1=location[0],location[1],location[2],location[3]
            cv.putText(fram,name,(y,x),cv.FONT_ITALIC,1,(0,0,800),2)
            cv.rectangle(fram,(x,y),(x1,y1),(0,0,200),4)
            if(name==z):
                if cv.waitKey(2) & 0xFF == ord(' '):
                    return 1
            else:
                if cv.waitKey(1) & 0xFF == ord(' '):
                    return 0
        cv.imshow('Frame', fram)
        key=cv.waitKey(1)