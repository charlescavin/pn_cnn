# author : Charles Cavin <charles@cavinai.com>

import csv
from utils.general_utils import PrintAndLog
from utils.psql_utils import psql_wrapper


# TODO: Document this program using docstrings
# This program:
# 1. Reads the mimic-cxr-2.0.0-chexpert.csv and mimic-cxr-2.0.0-negbio.csv
#    files.
# 2. Using a "strict" approach to positive (1) labels, accepts as a good
#    label only for those X-rays in which both chexpert and negbio assign
#    a '1' to the finding/no finding.
# 3. Sets anything not complying with the strict standard to '0'.
# 4. Creates a new csv file with the strict labeling standard for each
#    subject/study combination.
# 5. Creates a new table for chexpert labels, negbio labels, and strict
#    labels in Postgresql. NB: I would usually use MySQL, but the new
#    authentication module simply would not work for me.)
# 6. The new strict table/csv file will be used for modeling, starting with
#    Pleural Effusion, first for AP positions, then PA, both for subjects
#    standing erect.
# 7. Most of this has already been achieved using dataframes.


# Logging setup
filename = "logs/import_labels.log"
format = "%(levelname)s:%(asctime)s:%(message)s"
datefmt = "%H:%M:%S"

pl = PrintAndLog(filename, format, datefmt)
pl.print("Program started.")

# These csv files have identical structures
chex_labels = "data/csv/mimic-cxr-2.0.0-chexpert.csv"
negbio_labels = "data/csv/mimic-cxr-2.0.0-negbio.csv"
strict_labels = "data/csv/strict_labels.csv"

# Get user name and password for db
user = input("User name:  ")
passwd = input("Password:  ")

pw = psql_wrapper('localhost', 'pn', user, passwd)

# Open csv file containing all mimic chexpert records

files_and_tables = [[chex_labels, "chex_labels"],
                    [negbio_labels, "negbio_labels"]]

csv_label = 0
sql_table = 1

with open(chex_labels, 'r') as chex_file, \
        open(negbio_labels, 'r') as negbio_file, \
        open(strict_labels, 'w') as strict_file:

    chex_reader = csv.reader(chex_file, delimiter=',')
    negbio_reader = csv.reader(negbio_file, delimiter=',')
    strict_writer = csv.writer(strict_file, delimiter=',')

    # Use the chex_file column headings to insert underscores
    headers = next(chex_reader)

    cols = ''
    first = True
    for col in headers:
        if first is False:
            cols += ',' + col
        else:
            cols += col
            first = False

    # Skip the negbio header row
    next(negbio_reader)

    row_ctr = 0
    check_ctr = 0

    for index, (chex_row, negbio_row) in enumerate(zip(chex_reader,
                                                       negbio_reader)):

        chex_subject = chex_row[0]
        chex_study = chex_row[1]
        negbio_subject = negbio_row[0]
        negbio_study = negbio_row[1]

        # The chexpert and negbio label files have been sorted so the subject
        # and study order should be equal at every index, but just in case,
        # this code performs a final check to ensure they are equal.
        if chex_subject != negbio_subject or chex_study != negbio_study:
            pl.print("Problem: subject and/or study are not equal:")
            pl.print("Index: {index}")
            pl.print(f"Subject: chex:{chex_subject} negbio:{negbio_subject}")
            pl.print(f"Study: chex:{chex_study} negbio:{negbio_study}")
            break

        # Start query strings
        # For chex
        insert_chex_query = f"insert into chex_labels ({cols}) "
        insert_chex_query += f"values ({chex_row[0]},{chex_row[1]}"

        # For negbio
        insert_negbio_query = f"insert into negbio_labels ({cols}) "
        insert_negbio_query += f"values ({negbio_row[0]},{negbio_row[1]}"

        # For strict
        insert_strict_query = f"insert into strict_labels ({cols}) "
        insert_strict_query += f"values ({negbio_row[0]},{negbio_row[1]}"
        strict_csv = [negbio_row[0], negbio_row[1]]

        # Now go through each table and for each column after
        # subject ID and study ID to determine its value and
        # make it an int of 0 or 1
        new_values = {
                    '':     0,
                    '0.0':  0,
                    '1.0':  1,
                    '-1.0': 0}

        # Get values for each column in row
        for idx in range(2, 16):
            # For chex
            new_chex_value = new_values[chex_row[idx]]
            insert_chex_query += "," + str(new_chex_value)
            # For negbio
            new_negbio_value = new_values[negbio_row[idx]]
            insert_negbio_query += "," + str(new_negbio_value)
            # For strict
            if new_chex_value == 1 and new_negbio_value == 1:
                strict_value = 1
            else:
                strict_value = 0
            strict_csv.append(strict_value)
            insert_strict_query += "," + str(strict_value)

        # Write row to strict_csv
        strict_writer.writerow(strict_csv)

        insert_chex_query += ')'
        insert_negbio_query += ')'
        insert_strict_query += ')'

        # Execute queries to insert rows
        pw.exec_query_commit(insert_chex_query)
        pw.exec_query_commit(insert_negbio_query)
        pw.exec_query_commit(insert_strict_query)

        row_ctr += 1
        if row_ctr % 10000 == 0:
            pl.print(f"Through row {row_ctr:,}")

pl.print(f"Added {row_ctr:,} rows in total.")

pw.close_connection()
