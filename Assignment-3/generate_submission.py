import os
import cv2 as cv
import numpy as np
import pandas as pd

test_path = "./Testing_Data_Prediction1/"
test_mask_data = pd.read_csv(os.path.join(test_path, 'masked_info.csv')).drop(['Unnamed: 0'],axis=1)
submission = []
for i in range(len(test_mask_data)):
    filename, y1, x1, y2, x2 = test_mask_data.loc[i,]
    image = cv.imread(os.path.join(test_path, filename))
    b, g, r = cv.split(image)
    result = np.zeros((256, 256))
    normalized_b = b/255
    normalized_g = g/255
    normalized_r = r/255
    for i in range(y1 , y1+75):
        for j in range(x1, x1+75):
            temp1 = filename + '_' + 'box1' + '_' +  str(i) + '_' + str(j) + '_'
            submission.append((temp1 + '0', normalized_b[i,j]))
            submission.append((temp1 + '1', normalized_g[i,j]))
            submission.append((temp1 + '2', normalized_r[i,j]))
    for i in range(y2 , y2+75):
        for j in range(x2, x2+75):
            temp1 = filename + '_' + 'box2' + '_' + str(i) + '_' + str(j) + '_'
            submission.append((temp1 + '0', normalized_b[i,j]))
            submission.append((temp1 + '1', normalized_g[i,j]))
            submission.append((temp1 + '2', normalized_r[i,j]))
    print(filename)
df = pd.DataFrame(submission, columns=['filename_box_pixel','value'])
df.to_csv(test_path + 'submission.csv', index=False)