import numpy as np
import logging
import sys
import csv

def write_headers(csv_files, data_paths):
    # csv_files is an array of all the open csv files
    # data_paths is an array of all the file paths for csv files
    #   

    # Take a slice of file paths by position from the positions 
    # array and pass to this function
    print(f"csv_files = {csv_files}")
    print(f"data_paths = {data_paths}")

    for p, csvfile in enumerate(csv_files):
        print(f"p = {p}, csv_file = {csvfile}, ")
    try:              
        csvfile.write_row("Num, Path, Rows, Cols, LIPV\n")
    except:
        print(f"Exception details: {sys.exc_info()[0]}")
        logging.exception(f"Could not write header for {data_paths[p]}")
        print(f"Could not write header for {data_paths[p]}")
        return False
    else:
        print(f"Header for {data_path[p]} successfully written")
        return True

def write_row(csv_file, row_of_data):

    try:
        csv_file.write(row_of_data)  
    except:
        logging.exception(f"Could not write row {row_of_data:,}")
        print(f"Could not write row {row_of_data:,}")
        return False
    else:
        logging.info(f"Row written: {row_of_data:,}")
        print(f"Row written: {row_of_data:,}")  
        return True     
        