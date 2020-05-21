# author : Guillaume Lemaitre <g.lemaitre58@gmail.com>,
# author : Charles Cavin <charles@cavinAI.com>,
# author : Vivek Kumar for conversion from DICOM to JPG
# license : MIT

import pydicom as dicom
import cv2
import numpy as np
import matplotlib.pyplot as plt

dcm_path = "/data8/pn/dcm/files/p10/p10000032/s50414267/"
dcm_name = "02aa804e-bde0afdd-112c0b34-7bc16630-4e384014"
dcm_ext = ".dcm"

jpg_path = "/data4/pn/example_jpg/"
jpg_name = dcm_name
jpg_ext = ".jpg"
# ds = dicom.dcmread(dcm_path + dcm_name + dcm_ext)
ds = dicom.dcmread("/data8/pn/dcm/files/p10/p10462639/s58996083/637acaed-f7542d86-eb99d614-46270fc5-e01e748c.dcm")
print(f"Data type of ds: {type(ds)}")

pixel_array = ds.pixel_array

# Some metrics
print(f"pixel_array shape: {pixel_array.shape}")
print(f"max element in pixel_array: {np.amax(pixel_array):,}")
print(f"min element in pixel_array: {np.amin(pixel_array):,}")
print(f"avg element in pixel_array: {np.average(pixel_array):,}")
lipv = ds.LargestImagePixelValue
print(f"Largest image pixel value: {lipv:,}")

# Normalize, then convert to B&W
pixel_array_numpy = ((pixel_array / lipv) * 255).astype(int)
print(f"New max value in pixel_array_numpy: {np.amax(pixel_array_numpy)}")
cv2.imwrite(jpg_path + jpg_name + jpg_ext, pixel_array_numpy)

print(f"rows:       {int(ds.Rows):,}")
print(f"cols:       {int(ds.Columns):,}")
print(f"Image size: {len(ds.PixelData):,}")


# plot the image using matplotlib
plt.imshow(pixel_array_numpy, cmap='gray')
plt.show()
