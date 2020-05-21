import csv
import pydicom as dicom
import numpy as np
from pathlib import Path
import max_value_of_pixels_per_pos as mvpp
import sys
import time

# TODO:
# 1. Save the max pixel values in a csv file
# 2. Determine wether this should be done by machine
# csv file with dcm image paths and metadata

class Max_Pixels:

    def __init__(self):
        self.pn_data_file = "/home/cc/dev/CV/PhysioNet/pn_data.csv"
        self.max_pixel_values_file = "/home/cc/dev/CV/PhysioNet/max_pixel_values.csv"
        self.elapsed_time = 0
        self.est_time_remaining = 0
        self.num_of_images = 377110

    def save_max_value_of_pixels_per_position(self):
        # print("Gets into save_max_value_of_pixels_per_position(self)")
        start_time = time.process_time()
        max_pixel_values_by_pos = {}

        with open (self.pn_data_file, 'r', newline='') as csvfile:
            dcm_reader = csv.DictReader(csvfile, delimiter=',')
            row_ctr = 0
            for row in dcm_reader:
                ds = dicom.dcmread(row['Path'])
                
                if row_ctr == 50000:
                    break
                
                pos = row['Pos']
                if pos == 'antero-posterior':
                    max_pixel_in_this_image = np.amax(ds.pixel_array)

                    if pos in max_pixel_values_by_pos:
                        if max_pixel_in_this_image > max_pixel_values_by_pos[pos]:
                            max_pixel_values_by_pos[pos] = max_pixel_in_this_image
                    else:
                        max_pixel_values_by_pos[pos] = max_pixel_in_this_image
                    row_ctr += 1
                    # if row_ctr == 1:                
                    if row_ctr % 100 == 0:
                        print( "Rows read:", str(row_ctr), "pos:", pos, "mpv:", max_pixel_values_by_pos[pos] )
                        et = time.process_time() - start_time
                        etr = (self.num_of_images * et) / (row_ctr * 3600)
                        print("Time Elapsed: {:8.1f}, Est. Time Remaining: {:8.1f}".format(et, etr))
                        print("Max pixel in current image:", max_pixel_in_this_image)     
                        print(max_pixel_values_by_pos)     

        with open (self.max_pixel_values_file, 'w', newline ='') as mpv_file:
            for pos, mpv in max_pixel_values_by_pos:
                dcm_writer = csv.writer(mpv_file, delimiter=',')
                dcm_writer.writerow([pos, mpv])

    def get_max_value_of_pixels_per_position(self):
        # TODO: 
        #  1. If max_pixel_values.csv doesn't exist, 
        #     run save_max_value_of_pixels_per_position() - done
        #  2. Run a time counter to see elapsed time
        #     and time remaining for this function

        # print("Valid mpv file exists:", Path(self.max_pixel_values_file).is_file() )

        if Path(self.max_pixel_values_file).is_file() == False:
            self.save_max_value_of_pixels_per_position()

        max_pixel_values_by_pos = {}
        try:
            # print("Gets into 1st try")
            with open (max_pixel_values_file, 'r', newline='') as csvfile:
                dcm_reader = csv.DictReader(csvfile, delimiter=',')
        except:
            print("Could not open max_pixel_values file.")
            print(sys.exc_info()[0])
            return None
        else:
            for row in dcm_reader:
                pos = row['Pos']
                mpv = row['Max_Pixel_Value']
                max_pixel_values_by_pos[pos] = mpv
            return max_pixel_values_by_pos
       