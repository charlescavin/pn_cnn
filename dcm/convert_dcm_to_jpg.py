# author : Charles Cavin <charles@cavinAI.com>,
# license : MIT

import pydicom as dicom
import cv2
from utils.print_and_log import PrintAndLog

pl = PrintAndLog('/data8/pn/jpg/logs/convert_dcm_to_jpg')

# default lipv when none is present in dcm file
def_lipv = 4095


def dcm_to_jpg(dcm_path, jpg_path):

    try:
        dcm = dicom.dcmread(dcm_path)
    except dicom.errors.InvalidDicomError as error:
        pl.print(f'Could not read dicom file:')
        pl.print(f'Error: {error}')

    pixel_array = dcm.pixel_array

    lipv_in_dcm = 'LargestImagePixelValue' in dcm
    lipv = dcm.LargestImagePixelValue if lipv_in_dcm else def_lipv

    # Normalize, convert to B&W, and save as jpg
    pixel_array = ((pixel_array / lipv) * 255).astype(int)

    try:
        cv2.imwrite(jpg_path, pixel_array)
    except Exception as error:
        pl.print(f'Could not save jpg file:')
        pl.print(f'Error: {error}')
