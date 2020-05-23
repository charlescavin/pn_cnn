# author : Charles Cavin <charles@cavinAI.com>
# license : MIT

import glob
import pydicom as dicom
from pathlib import Path
from dcm.convert_dcm_to_jpg import dcm_to_jpg
from utils.print_and_log import PrintAndLog
from utils.process_time import ProcessTime

# =================== Set up Key Variables =====================
# Total number of images
TOT_DCMS = 377_110
# For displaying intermediate results while the program runs
BATCH_SIZE = 10_000
# Path to dcm files
PATH_TO_DCMS = "/data8/pn/dcm/files/p*/p*/s*/*.dcm"
# Path to jpg files
PATH_TO_JPGS = "/data8/pn/jpg/files/converted/"
# Path to log file
PATH_TO_LOGFILE = "/data8/pn/jpg/data/logs/dcm_to_jpg.log"
# ==============================================================

# Logging
pl = PrintAndLog(PATH_TO_LOGFILE)
paths = glob.iglob(PATH_TO_DCMS, recursive=True)
dcm_ctr = 0

# Track time required to convert files
pt = ProcessTime(TOT_DCMS, BATCH_SIZE)
start_time = pt.initiate()
pl.print("=======================================================")
pl.print(f"Start time:  {start_time}")
pl.print(f"Progress will be assessed for batches of", end=True)
pl.print(f"Batch size: {BATCH_SIZE:,}")

for path in paths:
    ds = dicom.dcmread(path)
    filename = Path(path).stem
    dcm_to_jpg(path, PATH_TO_JPGS + filename + ".jpg")
    dcm_ctr += 1
    if dcm_ctr % BATCH_SIZE == 0:
        # Get time_for_batch, time_since_start, projected_completion
        tfb, tss, pc = pt.batch_timing()
        pl.print("=======================================================")
        pl.print(f"Time taken for this batch:\t\t {tfb}")
        pl.print(f"Total dicoms converted:\t\t\t {dcm_ctr:,}")
        pl.print(f"Time taken since start:\t\t\t {tss}")
        pl.print(f"Projected time of completion:\t\t {pc}")

# Get total time taken and the time the process ended
tt, et = pt.end_proc()
pl.print("=======================================================")
pl.print("=======================================================")
pl.print("Final Values")
pl.print("=======================================================")
pl.print(f"Total time taken to convert dcms:\t {tt}")
pl.print(f"Time that process finished:\t {et}")
pl.print(f"Total files converted:\t\t\t {dcm_ctr:,}")
pl.print("=======================================================")
