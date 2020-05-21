# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
import pydicom as dicom
import os
import cv2

folder_path = "stage_1_test_images"  # Specify the output jpg/png folder path
jpg_folder_path = "JPG_test"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    image = image.replace('.dcm', '.jpg')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))
print('{} Total images converted'.format(n))
