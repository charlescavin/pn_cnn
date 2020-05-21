# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>, Charles Cavin <charles@cavinAI.com>, 
# Vivek Kumar for conversion from DICOM to JPG
# license : MIT

import pydicom as dicom
from pydicom.sequence import Sequence
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_path = "/data8/physionet.org/files/mimic-cxr/2.0.0/files/p10/p10000032/s50414267/"
image_name = "02aa804e-bde0afdd-112c0b34-7bc16630-4e384014"
output_path = "/data/PhysioNet/Example_JPG/"# Specify the output jpg/png folder path
jpg_folder_path = "JPG_test"
ds = dicom.filereader.dcmread(os.path.join(input_path, image_name + '.dcm'))

print ("View Code Sequence")
position = ds.ViewCodeSequence[0].CodeMeaning
print(position)

# Create function to return the patient position for the image
# return position

#print()
#print(ds)


pixel_array_numpy = ds.pixel_array
print('ds.pixel_array shape:', ds.pixel_array.shape)
print('Shape of pixel_array_numpy:', pixel_array_numpy.shape)
print('Elements of pixel_array_numpy', pixel_array_numpy)
print('max element in pixel array_numpy', np.amax(pixel_array_numpy))
print('min element in pixel array_numpy', np.amin(pixel_array_numpy))
print('avg element in pixel array_numpy', np.average(pixel_array_numpy))
# pixel_array_numpy = pixel_array_numpy / int(ds.LargestImagePixelValue)
# cv2.imwrite(os.path.join(output_path, image_name + '.jpg'), pixel_array_numpy)


print('Look at DICOM File')

if 'PixelData' in ds:
    print('PixelData is in ds')
    rows = int(ds.Rows)
    cols = int(ds.Columns)
    lipv = int(ds.LargestImagePixelValue)
    print("Image size: {rows:d} x {cols:d}, {size:d} bytes".format(
        rows=rows, cols=cols, size=len(ds.PixelData)))
    print("Largest image pixel value = {lipv:d}".format(lipv=lipv))
    #if 'PixelSpacing' in ds:
    #    print("Pixel spacing....:", ds.PixelSpacing)

# use .get() if not sure the item exists, and want a default value if missing
# print("Slice location...:", ds.get('SliceLocation', "(missing)"))

# plot the image using matplotlib
# plt.imshow(ds.pixel_array)
# plt.show()
