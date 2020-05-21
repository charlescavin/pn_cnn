# author : Charles Cavin <charles@cavinAI.com>
#
# license : MIT

import csv
import glob
import logging
import os
from datetime import datetime
from code.util import get_root_pn_dir


def extract_dicom_id(path):
    file_name = os.path.basename(path)
    return file_name.replace(".jpg", "")


# Logging
logging.basicConfig(
    filename="/home/cc/dev/cv/pn/logs/count_jpgs.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s:%(asctime)s:%(message)s",
    datefmt="%H:%M:%S"
)

rcd_ctr = 0
interval = 10000
total_rcds = 377110
start_time = datetime.now()
interval_time = start_time

search_path = "/data8/jpg/files/p*/p*/s*/*.jpg"
jpg_paths_csv = get_root_pn_dir.py + "pn/data/jpg_file_paths.csv"

print(jpg_paths_csv)
input()

paths = glob.iglob(search_path, recursive=True)

with open(jpg_paths_csv, 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(["dicom_id", "path"])

    for image_path in paths:
        csv_writer.writerow([extract_dicom_id(image_path), image_path])
        rcd_ctr += 1

        if rcd_ctr % interval == 0:
            now = datetime.now()
            interval_time_taken = now - interval_time
            total_time_taken = now - start_time
            interval_time = now
            time_taken_per_rcd = total_time_taken / rcd_ctr

            logging.info(f"{rcd_ctr:,} records written at: {now}")
            logging.info(
                f"Time taken for this interval: {interval_time_taken}")
            logging.info(f"Time taken overall: {total_time_taken}")
            print(f"{rcd_ctr:,} files found at: {now}")
            print(f"Time taken for this interval: {interval_time_taken}")
            print(f"Time taken overall: {total_time_taken}")
            total_time_required = time_taken_per_rcd * total_rcds
            time_to_completion = total_time_required - total_time_taken + now
            print(f"Estimated time of completion: {time_to_completion}")
            print()
            print("==========================================================")
            print()

logging.info(f"Total number of records: {rcd_ctr}")
print(f"Total number of records:  {rcd_ctr}")
