# importing required libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2 as poop
import glob
import argparse
import os

from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image


plt.rcParams.update({'font.size': 20})
plt.rcParams['figure.figsize'] = [9,7]
plt.rcParams['figure.autolayout'] = True

# adjustable range of pixel values from 0 to 255

# n = 256

# building bin index for histogram

# ih = np.zeros(n, np.int32)
# for i in range(0, n):
#     ih[i] = int(i)

# When run, user input is requested in which the user can copy and paste the file path
# The file is then adjusted into a useable format

# User inputs folder
# Sort folders by type into respective arrays
# run calcHist
# Begin calculations

def file_handling():
    # Create lists for organization
    h760_list = []
    h770_list = []
    h780_list = []

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    folder_path = os.path.join(script_dir, "Images for code testing purposes")

    count = 0

    for file in os.listdir(folder_path):
        filename = os.fsdecode(file)
        if "760" in filename:
            h760_list.append(file)
            count = count + 1
        elif "770" in filename:
            h770_list.append(file)
            count = count + 1
        else: 
            h780_list.append(file)
            count = count + 1

    h760 = sum(np.array(h760_list))
    h770 = sum(np.array(h770_list))
    h780 = sum(np.array(h780_list))


file_handling()















