import cv2
import numpy as np 
from matplotlib import pyplot as plt


""" img = np.uint8(np.random.randint(0, 255, size = (5, 5)))
height, width = img.shape


new_dimension = (25, 25)
plt.plot()
resized = cv2.resize(img, new_dimension, interpolation=cv2.INTER_LINEAR)
plt.title("INTER_LINEAR")
plt.imshow(resized, cmap='gray') """

#create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(0)



kernel = np.array([
    [5,1,5],
    [1,-1,1],
    [5,1,5]
]) 

""" kernel = np.ones((3, 3))
sigma = 2 """
#Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")

#Read until video is completed
while(cap.isOpened()):

    

    #Capture frame-by-frame
    ret, frame = cap.read()
    

    if ret == True:
        

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        f = cv2.filter2D(gray, 2, kernel)

        
        #near_img = cv2.resize(gray, None, fx = 2, fy= 2, interpolation=cv2.INTER_NEAREST)
        #gray = np.float32(gray)
        height, width = frame.shape[:2]

        temp = cv2.resize(gray, (10, 10), interpolation=cv2.INTER_LINEAR)
        output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
        
        print(int(output[50, 50]))

        #Display the resulting frame 
        cv2.imshow('Frame', output)

        #Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()

cv2.destroyAllWindows()