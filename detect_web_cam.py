from ultralytics import YOLO
import cv2
import cvzone
import math
from detect_hand import detectHand


cap = cv2.VideoCapture(0)

model = YOLO("./best_model.pt")

yolo_map = ['10c', '2c', '3c', '4c',
            '5c', '6c', '7c', '8c', 
            '9c', 'Ac', '3h', 'Kc',
            'Qc', '10d', '2d', '3d',
            '4d', '5d', '6d', '7d', 
            '8d', '9d', 'Ad', 'Jd',
            'Kd', 'Qd', '10h', '2h',
            '3h', '4h', '5h', '6h',
            '7h', '8h', '9h', 'Ah',
            'Jh', 'Kh', 'Qh', '10s',
            '2s', '3s', '4s', '5s',
            '6s', '7s', '8s', '9s',
            'As', 'Js', 'Ks', 'Qs']

#capturing video
out = cv2.VideoWriter('video_cap.avi',  
                        cv2.VideoWriter_fourcc(*'MJPG'), 
                        10, (640,480)) 
while True:
    
    suc ,img = cap.read()
    # img = cv2.flip(img,1)
    res = model(img,stream = True,conf=0.5)
    # print(res)
    cards = []
    
    for r in res:
        boxes = r.boxes
        for b in boxes:
            #for cv2
            x1,y1,x2,y2 = b.xyxy[0]
            x1,y1,x2,y2  = int(x1),int(y1),int(x2),int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(34,23,133),3)
            # print(x1,y1,x2,y2)
            
            bbox = int(x1),int(y1),int(x2-x1),int(y2-y1)
            cvzone.cornerRect(img,bbox)
            conf = (math.ceil(b.conf*100))/100 #0.343553 to 0.34
            cla = int(b.cls[0])
            # print(cla ,yolo_map[cla])
            
            hand_res = 0
            if(conf>0.5):
                cards.append(yolo_map[cla])
            if len(cards)==5:
                hand_res = detectHand(cards)
                cvzone.putTextRect(img,f'Your hand:{hand_res}',(100,50),scale=2)
            
            print(hand_res)
            cvzone.putTextRect(img,f'{conf} {yolo_map[cla]}',(max(0,x1),max(30,y1)),scale=1,thickness=1,offset=0)
            # cv2.putText(img,str(conf),(int(x1),int(y2-10)),cv2.FONT_HERSHEY_SIMPLEX,1,(25,25,134),2,cv2.LINE_AA)
            
    # img_f = cv2.flip(img,1)
    # img = cv2.resize(img,(640,480))
    out.write(img)
    cv2.imshow("sds",img)
    intr = cv2.waitKey(1)
    if intr & 0xFF == ord('q') :
        break