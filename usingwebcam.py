
#%%
import cv2, time

#%%
video = cv2.VideoCapture(0,cv2.CAP_DSHOW) #if one webcame then pass 0 if two pass 1 and so on 

#Check if the webcam is opened correctly
# if not camera.isOpened():
#     raise IOError("Cannot open webcam")

# return_value, image = camera.read()
# print("We take a picture of you, check the folder")
# cv2.imwrite("image.png", image)
a = 0
while True:
    a += 1
    check,frame = video.read() # Check is Boolean , Frame is numpy array 
    # print(check)
    # print(frame)
    #time.sleep(3)
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release() # Error is here
cv2.destroyAllWindows()
# %%
