# author : Charles Cavin <charles@cavinAI.com>
#
# license : MIT

import pydicom as dicom
import glob
import csv
import numpy as np
import logging
from datetime import datetime

# Logging
logging.basicConfig(
    filename="/home/cc/dev/CV/PhysioNet/Logs/get_meta_data.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s:%(asctime)s:%(message)s",
    datefmt="%H:%M:%S"
)

total_rcds = 377110
rcd_ctr = 1
interval = 1000
pn_data = "/home/cc/dev/CV/PhysioNet/csv_files/pn_data.csv"
start_time = datetime.now()
interval_time = start_time

with open(pn_data, 'w', newline='') as csvfile:
    header = ['Num', 'Pos', 'Path', 'Rows', 'Cols', 'LIPV']
    csv_writer = csv.writer(csvfile, delimiter=',')
    try:
        csv_writer.writerow(header)
    except:
        logging.exception("Could not write header")
        print("Could not write header")

    logging.info("Start of writing rows to csv file")
    print("Start of writing rows to csv file")

    paths = glob.iglob(
        "/data8/physionet.org/files/mimic-cxr/2.0.0/files/p*/p*/s*/*.dcm", recursive=True)
    num_of_nones = 0
    num_of_no_lipvs = 0
    num_of_no_pixel_arrays = 0
    logging.info("Starting to get meta data")
    print("Starting to get meta data")
    for dcm_path in paths:
        ds = dicom.dcmread(dcm_path)

        # Get the rows and columns
        rows = ds.Rows
        cols = ds.Columns

        # Get the patient position
        try:
            pos = ds[0x0054, 0x0220][0][0x0008, 0x0104].value
        except:
            logging.info(
                f"No position available for {dcm_path}, assuming 'none'")
            # print(f"No position available for {path}, assuming 'none'")
            pos = 'none'
            num_of_nones += 1

        # Get the Largest Image Pixel Value for normalizing in jpeg
        try:
            lipv = ds.LargestImagePixelValue
        except:
            logging.info(f"Largest pixel value for {dcm_path} does not exist")
            num_of_no_lipvs += 1
            try:
                lipv = np.amax(ds.pixel_array)
            except:
                logging.info(f"No pixel_array found in {dcm_path}")
                lipv = -1
                num_of_no_pixel_arrays += 1

        # Remove common part of path to save storage space
        short_path = dcm_path.replace(
            "/data8/physionet.org/files/mimic-cxr/2.0.0/files/", "")
        # Header is 'Num', 'Pos', 'Path', 'Rows', 'Cols','LIPV'
        row_of_data = [rcd_ctr, pos, short_path, rows, cols, lipv]
        # print(f"row_of_data:  {row_of_data}")

        # Write the row of data to the csv file
        try:
            csv_writer.writerow(row_of_data)
        except:
            logging.info(f"Row could not be written for {row_of_data}")
            print(f"Row could not be written for {row_of_data}")
        else:
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
                print(f"{rcd_ctr:,} records written at: {now}")
                print(f"Time taken for this interval: {interval_time_taken}")
                print(f"Time taken overall: {total_time_taken}")
                print(f"Projected time of completion in hours: \
                    {(((time_taken_per_rcd * total_rcds)) / 3600) - total_time_taken}")

logging.info(f"Number of records: {rcd_ctr}")
print(f"Number of records:  {rcd_ctr}")
logging.info(
    f"num_of_nones = {num_of_nones}, num_of_no_lipvs = {num_of_no_lipvs}, num_of_no_pixel_arrays = {num_of_no_pixel_arrays}")
print(
    f"num_of_nones = {num_of_nones}, num_of_no_lipvs = {num_of_no_lipvs}, num_of_no_pixel_arrays = {num_of_no_pixel_arrays}")
