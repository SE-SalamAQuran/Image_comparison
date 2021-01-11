from math import log10, sqrt 
import cv2 
import numpy as np 


##This is the first approach to achieve the goal
## Calculating MSE 'MEAN SQUARE ERROR" and then PSNR 'PEAK SIGNAL 2 NOISE RATIO'



def psnr(original, compressed):  #Calculate Peak Signal to Noise Ratio
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr 
  
def main(): 
     original = cv2.imread("./images/image_original.jpg") 
     compressed = cv2.imread("./images/image_contrast.jpg", 1) 
     value = psnr(original, compressed) 
     print(f"PSNR value is {value} dB") 
       
if __name__ == "__main__": 
    main() 