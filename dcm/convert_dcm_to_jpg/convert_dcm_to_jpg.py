file:///home/cc/dev/cv/pn/dcm/convert_dicom_to_jpg.py {"mtime":1590014688894,"ctime":1588192822588,"size":4441,"etag":"3552fd3qe4j8","orphaned":false}
# author : Charles Cavin <charles@cavinAI.com>
import csv
import glob
import pydicom as dicom
import numpy as np
import sys
from utils.print_and_log import PrintAndLog
from utils.process_time import ProcessTime

# I used codify.py from
# https://pydicom.github.io/pydicom/1.1/writing_files.html
# to get the correct codes for patient position (pos) and
# patient orientation (po)

# The file in which the results will be stored
pn_data = "/data8/pn/dcm/meta/pn_dcm_data.csv"
# The total number of dcm files
NUM_OF_DCM_FILES = 377_110
# The number of files to process in a batch
DCM_BATCH = 10_000
# The default maximum value of a dicom pixel
DEF_LIPV = 4_095
# The file and directory pattern for finding dcms
PATH_TO_DCMS = "/data8/pn/dcm/files/p*/p*/s*/*.dcm"
# A string of equal signs to separate lines of output
sep = "===================================================================="

postions = {
    'postero-anterior': 'pa',
    'antero-posterior': 'ap',
    'lateral': 'lat',
    'left anterior oblique': 'lao',
    'left lateral': 'll'}

# Logging
pl = PrintAndLog('/data8/pn/dcm/logs/dicom_to_jpg')

# Confirm that glob finds 377_100 dcm files
num_of_dcm_files = len(glob.glob(PATH_TO_DCMS))
if num_of_dcm_files != NUM_OF_DCM_FILES:
    pl.print(f"Number of dcm files is not {NUM_OF_DCM_FILES:,}")
    sys.exit()
else:
    pl.print(f"Number of dcm files, {num_of_dcm_files}, is correct")

# Tracking progress
pt = ProcessTime(num_of_dcm_files, DCM_BATCH)

paths = glob.iglob("/data8/pn/dcm/files/p*/p*/s*/*.dcm", recursive=True)
row = 0
no_po = 0
no_pos = 0

start_time = pt.initiate()

pl.print(sep)
pl.print(f"Started Program")

with open(pn_data, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    header = ['Row', 'Path', 'Pos', 'PO', 'Rows', 'Cols', 'LIPV']
    try:
        csv_writer.writerow(header)
    except Exception as error:
        pl.print("Could not write header")
        pl.print(f"error: {error}")

    for path in paths:
        dcm = dicom.dcmread(path)

        # Get the rows and columns
        rows = dcm.Rows
        cols = dcm.Columns

        # Get the patient position (anterior-posterior, lateral, etc.)
        vp_bool = 'ViewCodeSequence' in dcm
        cm_bool = len(dcm.ViewCodeSequence) > 0
        if vp_bool is True and cm_bool is True:
            pos = dcm.ViewCodeSequence[0].CodeMeaning
        else:
            pos = 'none'
            no_pos += 1

        # Get the patient orientation (erect, supine,etc.)
        pocs_bool = 'PatientOrientationCodeSequence' in dcm
        cm_bool = len(dcm.PatientOrientationCodeSequence) > 0
        if pocs_bool is True and cm_bool is True:
            po = dcm.PatientOrientationCodeSequence[0].CodeMeaning
        else:
            po = 'none'
            no_po += 1

        # Get the Largest Image Pixel Value
        if 'LargestImagePixelValue' in dcm is True:
            lipv = dcm.LargestImagePixelValue
        elif 'pixel_array' in dcm:
            lipv = np.amax(dcm.pixel_array)
        else:
            lipv = DEF_LIPV

        try:
            csv_writer.writerow([row, path, pos, po, rows, cols, lipv])
        except Exception as error:
            pl.print(f"Could not write row {row:,}")
            pl.print(f"error: {error}")

        # All processing for the current row completed so increment row
        row += 1

        if row % DCM_BATCH == 0:
            # Get time_for_batch, time_since_start, projected_completion
            tfb, tss, pc = pt.batch_check()
            pl.print(sep)
            pl.print(f"Current time:\t\t\t\t\t{pt.current_time()}")
            pl.print(f"Time taken for last batch:\t\t\t{tfb}")
            pl.print(f"Time taken since start:\t\t\t\t{tss}")
            pl.print(f"Projected time of completion:\t\t\t{pc}")
            pl.print(f"Number of rows added to csv:\t\t\t{row:,}")

    # Final values
    # Get total time taken and time the process ended

    tt, et = pt.end_proc()
    pl.print(sep)
    pl.print(sep)
    pl.print("Final Values")
    pl.print(sep)
    pl.print(sep)
    pl.print(f"Time the process started:\t\t\t{start_time}")
    pl.print(f"Total time elapsed processing dcm files:\t{tt}")
    pl.print(f"Number of files processed:\t\t\t{row}")
    pl.print(f"Time the process ended:\t\t\t\t{et:}")
    pl.print(f"Number without patient position:\t\t\t\t{no_pos}")
    pl.print(f"Number without patient orientation:\t\t{no_po}")
