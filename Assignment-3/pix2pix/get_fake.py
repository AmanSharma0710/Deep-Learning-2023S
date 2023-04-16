import os
import numpy as np
import cv2 as cv

PATH_TO_IMAGES= "C:/Users/sharm/Desktop/pytorch-CycleGAN-and-pix2pix/results/pix2pix_inpainting/test_latest/images/"
#Get all the images whose name ends with fake.png
images = [img for img in os.listdir(PATH_TO_IMAGES) if img.split(".")[0].endswith("fake")]
PATH_TO_DESTINATION = "C:/Users/sharm/Desktop/Deep-Learning-2023S/Assignment-3/Testing_Data_Prediction3/"
for image in images:
    name = image.split(".")[0][:-5] + "." +  image.split(".")[1]
    print(name)
    img = cv.imread(PATH_TO_IMAGES + image)
    cv.imwrite(os.path.join(PATH_TO_DESTINATION, name), img)
