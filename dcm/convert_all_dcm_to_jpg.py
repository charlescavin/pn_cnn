# author : Charles Cavin <charles@cavinai.com>

import glob
import pydicom as dicom
from pathlib import Path
from dcm.convert_dcm_to_jpg import dcm_to_jpg
from utils.print_and_log import PrintAndLog
from utils.process_time import ProcessTime

# =================== Set up Key Variables =====================
# Total number of images
tot_dcms = 377_110
# For displaying intermediate results while the program runs
interval_dcms = 10_000
# Logging
pl = PrintAndLog("/data8/pn/jpg/data/logs/dcm_to_jpg.log")
# Path to dcm files
path_to_dcms = "/data8/pn/dcm/files/p*/p*/s*/*.dcm"
# Path to jpg files
path_to_jpgs = "/data8/pn/jpg/files/converted/"
# ==============================================================

paths = glob.iglob(path_to_dcms, recursive=True)
dcm_ctr = 0

# Track time required to convert files
pt = ProcessTime(tot_dcms)
start_time = pt.get_start_time()
pl.print("=======================================================")
pl.print(f"Start time:  {start_time:%Y-%m-%d  %H:%M:%S}")
pl.print(f"Progress will be assessed for batches of", end=True)
pl.print(f"{interval_dcms:,}")

for path in paths:
    ds = dicom.dcmread(path)
    filename = Path(path).stem

    dcm_ctr += 1
    if dcm_ctr % interval_dcms == 0:
        # Get time_since_interim, time_since_start, project_completion
        tsi, tss, pc = pt.interim_check(dcm_ctr)
        pl.print("=======================================================")
        pl.print(f"Time taken for this batch:\t\t {pt.timedelta_fmt(tsi)}")
        pl.print(f"Total dicoms converted:\t\t\t {dcm_ctr:,}")
        pl.print(f"Time taken since start:\t\t\t {pt.timedelta_fmt(tss)}")
        pl.print(f"Projected time of completion:\t\t {pc:%Y-%m-%d  %H:%M:%S}")

    dcm_to_jpg(path, path_to_jpgs + filename + ".jpg")

# Get total time taken and the time the process ended
tt, et = pt.end_proc()
pl.print("=======================================================")
pl.print("=======================================================")
pl.print("Final Values")
pl.print("=======================================================")
pl.print(f"Total time taken to convert dcms:\t {tt}")
pl.print(f"Time that process finished:\t {et:%Y-%m-%d  %H:%M:%S}")
pl.print(f"Total files converted:\t\t\t {dcm_ctr}")
pl.print("=======================================================")
