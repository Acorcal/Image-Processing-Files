# importing required libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2 as poop
import glob
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams.update({'font.size': 20})
plt.rcParams['figure.figsize'] = [9,7]
plt.rcParams['figure.autolayout'] = True
# Changeable file type e.g(.jpg,.png,etc.) must be within **

file_type = "*.jpg*"

# adjustable range of pixel values from 0 to 255

n = 256

# building bin index for histogram

ih = np.zeros(n, np.int32)
for i in range(0, n):
    ih[i] = int(i)

# When run, user input is requested in which the user can copy and paste the file path
# The file is then adjusted into a useable format

for i in range(0, 1):

    path = 'C:\\Users\\alvin\\Downloads\\New Pictures 2-10-24-20240401T211154Z-001\\New Pictures 2-10-24\\Paper Fire Images'
    count = path.count('\\')
    count2 = path.count('"')
    if count != 0:
       new_path = path.replace('\\', '/')
    if count2 != 0:
        new_path = path.replace('"','')
    if path.endswith('/' + file_type):
        break
    elif path.endswith('/'):
        new_path = ''.join([path,file_type])
    else:
        new_path += '/'+ file_type
