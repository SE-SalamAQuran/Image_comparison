from numpy.core.fromnumeric import reshape, size
from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import cv2
import json
import math

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,	help="first input image")
ap.add_argument("-s", "--second", required=True, help="second")
ap.add_argument("-k", "--key", required=True, help="api-key")    
args = vars(ap.parse_args())

# load the two input images + API key
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
key = args["key"]
f = open("keys.json", 'r')
# returns JSON object as  a dictionary 
data = json.load(f) 


#check validation, i,e: if the key exists in our list of keys
def validate_key(api_key):
    result = False
    i=0
    for i in range(len(data['secret_keys'])):
        if api_key == data['secret_keys'][i]['key']:
            result = True
        else:
            result = False
        i+=1
        return result



#If the used enters a wrong api key, the  program will exit and issue an error message

if(not validate_key(key)):
    print("Wrong access key")
    exit()

#After checking that all inputs are valid we start the sequence of processes


# Resizing both images on a fixed scale
#Without this, the program will fail to compare between images of different sizes/dimensions

#Resizing only executes when the two images have different dimensions
#If the sizes are the same the program will skip to the next step, which is converting the images to grayscale

if imageA.size != imageB.size:
    scale_percent = 60 # percent of original size
    width = int(imageA.shape[1] * scale_percent / 100)
    height = int(imageA.shape[0] * scale_percent / 100)
    dim = (width, height)
  
# resize both images
    imageA = cv2.resize(imageA, dim, interpolation = cv2.INTER_AREA)
    imageB = cv2.resize(imageB, dim, interpolation =  cv2.INTER_AREA)


#Now the two images have the same dimensions
# convert the images to grayscale
#Why gray scale?
#Because the two images will have different color channels and we must make them the same
#  in the computer's point of view.

grayA = cv2.cvtColor(src=imageA, code=cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(src=imageB, code=cv2.COLOR_BGR2GRAY)

#Now that we have two images of the same size and color channel 

#We compute the Structural Similarity Index Measure (SSIM) between the two
# images, ensuring that the difference image is returned

(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("Similarity percentage: {} %".format(score * 100))
print("Rounded result is: ", round(score * 100, 2), "%")
