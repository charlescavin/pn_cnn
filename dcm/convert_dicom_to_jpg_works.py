# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>, Charles Cavin <charles@cavinAI.com>, Vivek Kumar
import pydicom as dicom
from pydicom.data import get_testdata_files
import os
import cv2
import numpy as np
import time
import glob as glob
import re
import h5py
from pathlib import Path

def load_dcm():
    t0 = time.clock()
    print("Loading dicom file paths from glob")
    filepath_to_dcms = glob.glob('/data8/physionet.org/files/mimic-cxr/2.0.0/files/p*/p*/s*/*.dcm', recursive=True)
    # print('dtype of fp_train = ', fp_train)
    print("Elapsed time to load training file paths using glob: ", time.clock() - t0)
    save_dcm_file_paths(filepath_to_dcms)

# Continue by adding paths to .txt file
def save_dcm_file_paths(filepath_to_dcms):
    t0 = time.time()
    print("filepath_to_dcms_len = ", len(filepath_to_dcms)) 
    with open("/data/PhysioNet/FilePaths/dcm_file_paths.txt", "w") as filehandle:
        for file_path in filepath_to_dcms:
            filehandle.write('%s\n' % file_path)

    print("Elapsed time to save training file paths as .txt: ", time.time() - t0)

load_dcm()


    