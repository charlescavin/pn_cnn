### This did not work!

import numpy as np
import logging
import sys

dcm_matrix = np.genfromtxt("/Volumes/Data/JPG_files/physionet.org/files/mimic-cxr-jpg/dcm_matrix.csv",delimiter=',')

try:
    dcm_matrix = dcm_matrix[dcm_matrix[:,2].argsort()]
except:
    print("Matrix was not sorted")
else:
    print("End of matrix sorting")

try:
    np.savetxt("/Volumes/Data/JPG_files/physionet.org/files/mimic-cxr-jpg/dcm_matrix2.csv", dcm_matrix, delimiter=',')
except TypeError:
    print(f"Error is: {TypeError.with_traceback}")
    logging.exception("Could not save matrix to csv.")
    print(f"Could not save matrix to csv.")
    print(f"More error information: {sys.exc_info()[0]}")
