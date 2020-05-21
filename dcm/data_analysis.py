import pandas as pd
import sys

dicom_data_path = "/home/cc/dev/CV/PhysioNet/pn_data.csv"

# Return a DataFrame from the csv file
# def load_dicom_data(path):
try:
    dicom_data = pd.read_csv(dicom_data_path)
except Exception as error:
    print("Problem reading csv file in " + dicom_data_path)
    print(f"Error: {error}")
    print(sys.exc_info()[0])

'''
for row in range(0, 4):
    print(dicom_data.head().loc[[row]])
'''

print("Description of dicom_dataset:")
print(dicom_data.describe(include='Position'))
print("Unique values for position")
print(dicom_data.Pos.unique())
