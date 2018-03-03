from PIL import Image
import cv2
from skimage import morphology
import numpy as np

#image read
A=cv2.imread('nisarg.jpeg');
#set dimensions
I2 = cv2.resize(A,(800,800));
#convert to grey
gray = cv2.cvtColor(I2, cv2.COLOR_BGR2GRAY)
#convert to binary
gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#reverse colours
im=cv2.bitwise_not(gray)
cv2.imwrite('nisarg1.jpeg', gray)
cv2.imwrite('nisarg2.jpeg',im)
#remove noise
imge=morphology.remove_small_objects(im,30,8)
cv2.imwrite('nisarg4.jpeg',imge)
