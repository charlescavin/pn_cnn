import sys
import csv

# csv file with dcm image paths and metadata
pn_data_file = "/home/cc/dev/CV/PhysioNet/pn_data.csv"
ap_paths = []
total_records = 377100

try:
    with open(pn_data_file, 'r', newline='') as csvfile:
        print("Gets past with open")

        dcm_reader = csv.reader(csvfile, delimiter=',')
        print("Gets past csv_reader")
        n = 0
        for row in dcm_reader:
            if n != 0:
                print("row:", row)
                print("Gets past row in dcm_reader")
                print("Pos:", row['Pos'])
                if row['Pos'] == 'antero-posterior':
                    print("Gets into if statement")
                    ap_paths.append(row['Path'])
                    n += 1
                    if n % 1000 == 0:
                        print("Records processed: {:d}  Progress = {:d}%".format(n, int(n/total_records * 100)))
                        print("Estimated Time remaining")
            else:
                n += 1
        print("pn_data_file reading complete")

except:
    print("Problem with or inside open statement")
    print(sys.exc_info()[0])

num_of_rcds = len(ap_paths)

print("Number of rcds:", num_of_rcds)

