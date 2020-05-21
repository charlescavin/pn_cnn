import pydicom

filename = "/data8/pn/dcm/files/p10/p10999395/s50315575/6948c444-96391ca8-99b4ffc2-b91f9d4e-92529c73.dcm"
ds = pydicom.dcmread(filename)
print(ds)
# patient_orientation_ds = ds.PatientOrientation


"""
potential_hit = ds.dir("ImagePosition")
# print(potential_hit)
print(ds.PatientOrientation[0])
print(ds.ViewPosition)
"""
