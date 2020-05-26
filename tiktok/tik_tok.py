import numpy as np
import cv2
def click_event_1(event,x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        if x<= 171 and y <= 171:
            #1
            cv2.line(img, (20, 20), (151, 151), (0, 255, 0), 10)
            cv2.line(img, (151, 20), (20, 151), (0, 255, 0), 10)
        if x>=171 and x<=342 and y <= 171:
            # 2
            cv2.line(img, (191, 20), (322, 151), (0, 255, 0), 10)
            cv2.line(img, (322, 20), (191, 151), (0, 255, 0), 10)
        if x<= 512 and x>=342 and y <= 171:
            # 3
            cv2.line(img, (362, 20), (492, 151), (0, 255, 0), 10)
            cv2.line(img, (492, 20), (362, 151), (0, 255, 0), 10)
        if x<=171 and y>=171 and y<=342:
            # 4
            cv2.line(img, (20, 191), (151, 322), (0, 255, 0), 10)
            cv2.line(img, (20, 322), (151, 191), (0, 255, 0), 10)
        if x>=171 and x<=342 and y>=171 and y<=342:
            # 5
            cv2.line(img, (191, 191), (322, 322), (0, 255, 0), 10)
            cv2.line(img, (191, 322), (322, 191), (0, 255, 0), 10)
        if x>=342 and x<=512 and y>=171 and y<=342:
            # 6
            cv2.line(img, (362, 191), (492, 322), (0, 255, 0), 10)
            cv2.line(img, (492, 191), (362, 322), (0, 255, 0), 10)
        if x<=171and y>=342 and y<=512:
            # 7
            cv2.line(img, (20, 362), (151, 492), (0, 255, 0), 10)
            cv2.line(img, (151, 362), (20, 492), (0, 255, 0), 10)
        if x>=171 and x<=342 and y>=342 and y<=512:
            # 8
            cv2.line(img, (191, 362), (322, 492), (0, 255, 0), 10)
            cv2.line(img, (322, 362), (191, 492), (0, 255, 0), 10)
        if x>=342 and x<=512 and y>=342 and y<=512:
            # 9
            cv2.line(img, (362, 362), (492, 492), (0, 255, 0), 10)
            cv2.line(img, (492, 362), (362, 492), (0, 255, 0),10)

        if img[85,85,1]==255 and img[85,256,1]==255 and img[85,427,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[256,85,1]==255 and img[256,256,1]==255 and img[256,427,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[427,85,1]==255 and img[427,256,1]==255 and img[427,427,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,85,1]==255 and img[256,85,1]==255 and img[427,85,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,256, 1] == 255 and img[256, 256, 1] == 255 and img[427, 256, 1] == 255:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,427,1]==255 and img[256,427,1]==255 and img[427,427,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,85,1]==255 and img[256,256,1]==255 and img[427,427,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,427,1]==255 and img[256,256,1]==255 and img[427,85,1]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_1 WIN', (50, 175), font, 2, (255, 255, 255), 5)


    cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x,',',y)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #strXY = str(x) + ',' + str(y)
       # cv2.putText(img,strXY,(x,y),font,1,(0,0,255),1)


        if x <= 171 and y <= 171:
            cv2.circle(img, (86, 86), (60), (0, 0, 255), 10)
        if x >= 171 and x <= 342 and y <= 171:
            cv2.circle(img, (257, 86), (60), (0, 0, 255), 10)
        if x <= 512 and x >= 342 and y <= 171:
            cv2.circle(img, (428, 86), (60), (0, 0, 255), 10)
        if x <= 171 and y >= 171 and y <= 342:
            cv2.circle(img, (86, 257), (60), (0, 0, 255), 10)
        if x >= 171 and x <= 342 and y >= 171 and y <= 342:
            cv2.circle(img, (257, 257), (60), (0, 0, 255), 10)
        if x >= 342 and x <= 512 and y >= 171 and y <= 342:
            cv2.circle(img, (428, 257), (60), (0, 0, 255), 10)
        if x <= 171 and y >= 342 and y <= 512:
            cv2.circle(img, (86, 428), (60), (0, 0, 255), 10)
        if x >= 171 and x <= 342 and y >= 342 and y <= 512:
            cv2.circle(img, (257, 428), (60), (0, 0, 255), 10)
        if x >= 342 and x <= 512 and y >= 342 and y <= 512:
            cv2.circle(img, (428, 428), (60), (0, 0, 255), 10)


        if img[85,24,2]==255 and img[85,195,2]==255 and img[85,366,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[256,24,2]==255 and img[256,195,2]==255 and img[256,366,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[427,24,2]==255 and img[427,195,2]==255 and img[427,366,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,22,2]==255 and img[256,22,2]==255 and img[427,22,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,193, 2] == 255 and img[256, 193, 2] == 255 and img[427, 193, 2] == 255:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,364,2]==255 and img[256,364,2]==255 and img[427,364,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,24,2]==255 and img[256,195,2]==255 and img[427,366,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)

        elif img[85,366,2]==255 and img[256,195,2]==255 and img[427,24,2]==255:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'PLAYER_2 WIN', (50, 175), font, 2, (255, 255, 255), 5)


    cv2.imshow('image', img)

img = np.zeros((512,512,3),np.uint8)

img = cv2.line(img,(342,0),(342,512),(255,0,0),5)
img = cv2.line(img,(0,171),(512,171),(255,0,0),5)
img = cv2.line(img,(0,342),(512,342),(255,0,0),5)
img = cv2.line(img, (171, 0), (171, 512), (255, 0, 0), 5)

cv2.imshow('image',img)
print('PLAYER_1 = X,PLAYER_2 = O')
print (cv2.setMouseCallback('image',click_event_1))


cv2.waitKey(0)
cv2.destroyAllWindows()
