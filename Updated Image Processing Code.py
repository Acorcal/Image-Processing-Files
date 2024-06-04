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

    h760 = 0
    h770 = 0
    h780 = 0

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    folder_path = os.path.join(script_dir, "Images for code testing purposes")

    count = 0

    # This loop will take each file, turn it into a histogram, and then compare the original file name with the string subset to sort the histogram

    for file in os.listdir(folder_path):
        # Convert the file into a histogram by passing the file path to the function
        img_file = poop.imread(os.path.join(folder_path, file), 0)
        h_img = poop.calcHist([img_file], [0], None, [256], [0, 256])
        
        # Sort the files by nanometers, this is specifed in the file name
        filename = os.fsdecode(file)
        if "760" in filename:
            h760_list.append(h_img)
            count = count + 1
        elif "770" in filename:
            h770_list.append(h_img)
            count = count + 1
        elif "780" in filename: 
            h780_list.append(h_img)
            count = count + 1
        else:
            print("File did not match the specified format, input the nm in the name and then run again." + filename)

    h760 = sum(np.array(h760_list))
    h770 = sum(np.array(h770_list))
    h780 = sum(np.array(h780_list))

    return h760, h770, h780

    # print(len(h760_list))
    # print(len(h770_list))
    # print(len(h780_list))


file_handling()

# def main():
#     h760 = 0
#     h770 = 0
#     h780 - 0
    
#     h760, h770, h780 = file_handling()

#     histogram_processing(h760, h770, h780)












