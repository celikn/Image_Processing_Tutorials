import cv2
from matplotlib import pyplot as plt 
 
img =cv2.imread("320033569584635.jpg",1) # Color BGR in default
plt.imshow(img)
plt.show()

## Eger plot icin opencv kullaniyorsak RGB gosterir.
resized =cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
# cv2.imshow("original_im",img)
# cv2.imshow("resized_im",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## print bgr values of pixels in the image 
print("Top Left",img[0,0])
print("Top right",img[0,400])
print("bottom left",img[500,0])
print("bottom right",img[500,500])

#Split and merging channels ## herbiri birer gray image olur
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only

cv2.imshow("green pic", green)
# cv2.waitKey(0)          
# cv2.destroyAllWindows() 

## Merging all channels
img_merged = cv2.merge((blue,green,red))
cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

######################
# Opencv offers Many libraries for image processing tasks
#We cover a few of them in future but for now let us look at a simple example
#Edge detection:
    
import cv2

img = cv2.imread("480976409840746.jpg", 0)
edges = cv2.Canny(img,100,200)   #Image, min and max values

cv2.imshow("Original Image", img)
cv2.imshow("Canny", edges)

cv2.waitKey(0)          
cv2.destroyAllWindows() 