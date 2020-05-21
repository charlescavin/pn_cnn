# author : Charles Cavin <charles@cavinai.com>
import csv
import numpy as np
import logging
import sys
from csv_file_opns import write_headers, write_row
from general_utils import PrintAndLog
from process_time import process_time



# Total number of images
tot_rows = 377110

# Keep track of time required to process files
pt = process_time(tot_rows)

# For displaying intermediate results while the program runs
interval_rows = 1000

# Logging
pl = PrintAndLog("/data8/pn/jpg/data/logs/dcm_to_jpg.log")

# Write a separate csv file for each position to speed up processing
# These may be combined in the future for coterminous patient studies
ap_data = "/data8/pn/jpg/data/csv/ap_data.csv"
pa_data = "/data8/pn/jpg/data/csv/pa_data.csv"
lat_data = "/data8/pn/jpg/data/csv/lat_data.csv"
lao_data = "/data8/pn/jpg/data/csv/lao_data.csv"
ll_data = "/data8/pn/jpg/data/csv/ll_data.csv"
no_data = "/data8/pn/jpg/data/csv/no_data.csv"

# Main csv file containing all records
pn_data = "/data8/pn/jpg/data/csv/pn_data.csv"

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
    with open(pn_data, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        # The first line of data is the header which isn't needed
        next(csv_reader)

        for row in csv_reader:
            pos = np.where(positions == row[1])[0][0]
            # Delete the position from the row
            new_row = np.delete(row, 1)
            # Change the first column to the correct row from positions
            new_row[0] = positions[pos][row_ctr_idx]
            try:       
                # Write the row from pn_data to the associated csv file
                csv_file = open(positions[pos][csv_path_idx], 'a')
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow(new_row)
            except:
                logging.exception(f"Could not write row to {new_row[1]}")
                print(f"Could not write row to {new_row[1]}")
            else:
                csv_file.close
                logging.info(f"Wrote {new_row} to {new_row[1]}")
                pn_row_ctr += 1
                positions[pos][row_ctr_idx] = str(int(positions[pos][row_ctr_idx]) + 1)
                if pn_row_ctr % 1000 == 0:
                    now = datetime.now()
                    interval_time_taken = now - interval_time
                    total_time_taken = now - start_time
                    interval_time = now
                    logging.info(f"{pn_row_ctr:,} records written at: {now}")
                    logging.info(f"Time taken for this interval: {interval_time_taken}")
                    logging.info(f"Time taken overall: {total_time_taken}")
                    print(f"{pn_row_ctr:,} records written at: {now}")
                    print(f"Time taken for this interval: {interval_time_taken}")
                    print(f"Time taken overall: {total_time_taken}")
                    print(f"Projected time of completion in hours: {(((total_time_taken / pn_row_ctr) * tot_rows)) / 3600}")

 
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


# Close all open files
# After this, start on JPG conversion, starting with 'ap' and 'pa' files
