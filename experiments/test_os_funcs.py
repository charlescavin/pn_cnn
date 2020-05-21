import os

path = "/data8/jpg/files/myfile.txt"
file_name = os.path.basename(path)
dicom_id = file_name.replace(".txt", "")
path_part = os.path.dirname(path)

print(f"Path: {path_part}")
print(f"File name: {file_name}")

insert_row_query = f"insert into jpg_file_paths values ({dicom_id}, {path})"

print(insert_row_query)