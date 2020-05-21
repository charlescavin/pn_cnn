# author : Charles Cavin <charles@cavinai.com>
import csv
# import pydicom
import numpy as np
import logging
from datetime import datetime
# import sys
# from csv_file_opns import write_headers, write_row

#   ===> START HERE <===
start_time = datetime.now()
interval_time = start_time

# Total number of images
tot_rows = 374680
# For displaying intermediate results while the program runs
interval_rows = 1000

#Logging
logging.basicConfig(
    filename="/home/cc/dev/CV/PhysioNet/csv_files/DCM_to_JPG.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s:%(asctime)s:%(message)s",
    datefmt="%H:%M:%S"
    )

# Write a separate csv file for each position to speed up processing
# These may be combined in the future for conterminous patient studies
ap_data = "/home/cc/dev/CV/PhysioNet/csv_files/ap_data.csv"
pa_data = "/home/cc/dev/CV/PhysioNet/csv_files/pa_data.csv"
lat_data = "/home/cc/dev/CV/PhysioNet/csv_files/lat_data.csv"
lao_data = "/home/cc/dev/CV/PhysioNet/csv_files/lao_data.csv"
ll_data = "/home/cc/dev/CV/PhysioNet/csv_files/ll_data.csv"
no_data = "/home/cc/dev/CV/PhysioNet/csv_files/no_data.csv"

# Main csv file containing all records
pn_data = "/home/cc/dev/CV/PhysioNet/csv_files/pn_data.csv"

# 'positions' opens each csv file by position and contains:
# 1. The value of the patient position or 'none'
# 2. The path to the csv file to write
# 3. The variable for each position's file writer
# 4. The total number of rows for each position    
positions = np.array([ \
    ['antero-posterior', ap_data, 1],
    ['postero-anterior', pa_data, 1],
    ['lateral', lat_data, 1],
    ['left anterior oblique', lao_data, 1],
    ['left lateral', ll_data, 1],
    ['none', no_data, 1]
    ])

# These are indices for the 'positions' array above
pos_idx = 0
csv_path_idx = 1
row_ctr_idx = 2
header = ['Num', 'Path', 'Rows', 'Cols','LIPV']
pn_row_ctr = 0

# Write headers for each position file
for pos in positions:
    with open(pos[csv_path_idx], 'w', newline='') as csvfile:
        try:
            csv_writer = csv.writer(csvfile, delimiter = ',')
            csv_writer.writerow(header)
        except:
            logging.exception("Could not write header")
            print("Could not write header")

# Read each row of the pn_data file which contains the meta data
# and append rows to the files below per position
with open(pn_data, 'r') as pn_file, \
    open(ap_data, 'a') as ap_file, \
    open(pa_data, 'a') as pa_file, \
    open(lat_data, 'a') as lat_file, \
    open(lao_data, 'a') as lao_file, \
    open(ll_data, 'a') as ll_file, \
    open(no_data, 'a') as no_file:

    pos_files = [
        ap_file,
        pa_file,
        lat_file,
        lao_file,
        ll_file,
        no_file
        ]

    # Set up reader
    pn_file_reader = csv.reader(pn_file, delimiter=',')
    # And writers
    ap_file_writer = csv.writer(ap_file, delimiter=',')
    pa_file_writer = csv.writer(pa_file, delimiter=',')
    lat_file_writer = csv.writer(lat_file, delimiter=',')
    lao_file_writer = csv.writer(lao_file, delimiter=',')
    ll_file_writer = csv.writer(ll_file, delimiter=',')
    no_file_writer = csv.writer(no_file, delimiter=',')

    file_writers = [
        ap_file_writer,
        pa_file_writer,
        lat_file_writer,
        lao_file_writer,
        ll_file_writer,
        no_file_writer
    ]

    # The first line of data is the header which isn't needed   
    next(pn_file_reader)

    for row in pn_file_reader:
        # logging.info(f"row from pn_file_reader")
        # logging.info(f"{row}")
        pos = np.where(positions == row[1])[0][0]
        # logging.info(f"pos: {pos}")
        # Delete the position field from the row
        new_row = np.delete(row, 1)
        # Change the first column to the correct row number from positions
        new_row[0] = positions[pos][row_ctr_idx]
        # logging.info(f"new_row: {new_row}")
        #logging.info(f"position: {positions[pos][0]}")

        try:       
            # Write the row from pn_data to the associated csv file
            file_writers[pos].writerow(new_row)
            # logging.info(f"file_writers[pos]: {file_writers[pos]}")
        except:
            logging.exception(f"Could not write row to {new_row[1]}")
        else:
            #logging.info(f"Wrote {new_row} to {new_row[1]}")
            #logging.info(f"---------------------")
            #logging.info(f"---------------------")
            pn_row_ctr += 1
            positions[pos][row_ctr_idx] = int(positions[pos][row_ctr_idx]) + 1
            if pn_row_ctr % 1000 == 0:
                now = datetime.now()
                interval_time_taken = now - interval_time
                total_time_taken = now - start_time
                time_taken_per_row = total_time_taken / pn_row_ctr
                interval_time = now
                # logging.info(f"{pn_row_ctr:,} records written at: {now}")
                # logging.info(f"Time taken for this interval: {interval_time_taken}")
                # logging.info(f"Time taken overall: {total_time_taken}")
                print(f"{pn_row_ctr:,} records written at: {now}")
                print(f"Time taken for this interval: {interval_time_taken}")
                print(f"Time taken overall: {total_time_taken}")
                print(f"Projected time of completion: \
                        {(((time_taken_per_row * tot_rows)) / 3600) - total_time_taken + now}")


 
# Final values
finish_time = datetime.now()
logging.info("Final Values")
logging.info("------------")    
logging.info(f"Total time elapsed creating csvs: {finish_time - start_time }")
logging.info(f"Total number of ap's = {positions[0][2]}")         
logging.info(f"Total number of pa's = {positions[1][2]}")
logging.info(f"Total number of lat's = {positions[2][2]}")
logging.info(f"Total number of lao's = {positions[3][2]}")
logging.info(f"Total number of ll's = {positions[4][2]}")
logging.info(f"Total number of no's = {positions[5][2]}")
logging.info(f"Total number of records written = {pn_row_ctr}")
print(f"Final Values")
print(f"------------")
print(f"Total time elapsed creating csvs: {finish_time - start_time }")
print(f"Total number of ap's = {positions[0][2]}")         
print(f"Total number of pa's = {positions[1][2]}")
print(f"Total number of lat's = {positions[2][2]}")
print(f"Total number of lao's = {positions[3][2]}")
print(f"Total number of ll's = {positions[4][2]}")
print(f"Total number of no's = {positions[5][2]}")
print(f"Total number of records written = {pn_row_ctr}")

