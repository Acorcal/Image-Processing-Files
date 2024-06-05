# importing required libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2 as poop
import os
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams.update({'font.size': 20})
plt.rcParams['figure.figsize'] = [9,7]
plt.rcParams['figure.autolayout'] = True




def file_handling():
    # Create lists for organization
    h760_list = []
    h770_list = []
    h780_list = []

    h760 = 0
    h770 = 0
    h780 = 0

    # Building adjustable bin index for histograms

    n = 256
    ih = np.zeros(n, np.int32)
    
    # Find the folder path and turn it into a useable format

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    folder_path = os.path.join(script_dir, "Images for code testing purposes")
    print(folder_path)
    count = 0
    
    # This loop will take each file, turn it into a histogram, and then compare the original file name with the string subset to sort the histogram

    for file in os.listdir(folder_path):

        # Calculatre the histograms for each image manually
        img_file = poop.imread(os.path.join(folder_path,file),0)
        img_file_array = np.array(img_file)
        rows, cols = img_file_array
        for row in range(rows):
            for col in range(cols):
                pixel = img_file_array[row,col]
                ih[pixel] += 1

        # h_img = poop.calcHist([img_file],[0],None,[256],[0,256])
        # Sort the files by nanometers, this is specifed in the file name
        filename = os.fsdecode(file)
        if "760" in filename:
            h760_list.append(ih)
            count = count + 1
        elif "770" in filename:
            h770_list.append(ih)
            count = count + 1
        elif "780" in filename: 
            h780_list.append(ih)
            count = count + 1
        else:
            print("File did not match the specified format, input the nm in the mame and run again." + filename)


    h760 = sum(np.array(h760_list))
    h770 = sum(np.array(h770_list))
    h780 = sum(np.array(h780_list))
    
    
    return h760, h770, h780

    # print(len(h760_list))
    # print(len(h770_list))
    # print(len(h780_list))


file_handling()
## Test for writing to .txt

    # hfile = open('histogram data.txt',"w")
    # hfile.write(str(h760_list[0]))
    # hfile.close

    ## Required for comparison below

    # h760_array = np.array(h760_list)
    # firstpic = h760_array[0,:]
    # firstpic = firstpic.flatten()
    # return firstpic
    

    






# Testing accuracy of manual calculation to built-in function

# result = file_handling()
# M = poop.imread("C:\\Users\\alvin\\PycharmProjects\\5 pic histogram\\F_760_1.jpg",0)
# M_array = np.array(M)

# rows, cols = M_array.shape
# for row in range(rows):
#     for col in range(cols):
#         pixel = M_array[row,col]
#         ih[pixel] += 1
# htest = open('manual histogram.txt',"w")
# ih_array = np.array(ih)
# htest.write(str(ih))
# htest.close

# print(ih_array.shape)
# print(result.shape)
# if np.all(np.array(ih) == result):
#         print('1 to 1\n')
# else:
#     error = ((np.array(ih) - result))
#     print('Error index:\n ',error)
