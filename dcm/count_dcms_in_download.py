# author  : Charles Cavin <charles@cavinAI.com>
# license : MIT

import glob
import logging
from datetime import datetime

# Logging
logging.basicConfig(
    filename="/home/cc/dev/CV/PhysioNet/Logs/count_dcms.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s:%(asctime)s:%(message)s",
    datefmt="%H:%M:%S"
)

count_dcms = False
rcd_ctr = 0
interval = 10_000
total_rcds = 377_110
start_time = datetime.now()
interval_time = start_time

search_path = "/data8/pn/dcm/files/p*/p*/s*/*.dcm"

paths = glob.iglob(search_path, recursive=True)

for image_path in paths:
    rcd_ctr += 1

    if rcd_ctr % interval == 0:
        now = datetime.now()
        interval_time_taken = now - interval_time
        total_time_taken = now - start_time
        interval_time = now
        time_taken_per_rcd = total_time_taken / rcd_ctr

        logging.info(f"{rcd_ctr:,} records counted at: {now}")
        logging.info(
            f"Time taken for this interval: {interval_time_taken}")
        logging.info(f"Time taken overall: {total_time_taken}")
        print(f"{rcd_ctr:,} files found at: {now}")
        print(f"Time taken for this interval: {interval_time_taken}")
        print(f"Time taken overall: {total_time_taken}")
        # Projected time of completion
        ptc = ((time_taken_per_rcd * total_rcds) - total_time_taken) + now
        print(f"Projected time of completion: {ptc}")
        print()
        print("==========================================")
        print()

logging.info(f"Total number of records: {rcd_ctr}")
print(f"Total number of records:  {rcd_ctr}")
