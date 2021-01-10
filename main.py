from key_generator.key_generator import generate
from SSIM_PIL import compare_ssim
import cv2
import numpy as np
import PIL
from PIL import Image
from cv2 import cvtColor, COLOR_BGR2GRAY

from SSIM_PIL import compare_ssim
from PIL import Image
from numpy.lib.type_check import imag


url = "./images/image_edited.jpg"
img = cv2.imread(url)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def ssim():

    path1 = "./images/image_original.jpg"
    path2 = "./images/image_edited.jpg"
    

    src1 = cv2.imread(path1)
    src2 = cv2.imread(path2)

    image1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

    value = compare_ssim(image1, image2)
    return value


def mse(image1, image2):
    err = np.sum((image1.astype("float")) - (image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err

# img1 = cv2.imread("./images/image_original.jpg")
# img2 = cv2.imread("./images/image_edited.jpg")

from PIL import Image, ImageOps
import numpy as np

img = Image.open(url).convert('L')
img_inverted = ImageOps.invert(img)

np_img = np.array(img_inverted)
np_img[np_img > 0] = 1

print(np_img)










