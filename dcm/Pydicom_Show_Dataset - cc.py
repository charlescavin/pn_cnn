# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
# license : MIT

from __future__ import print_function

import pydicom

print(__doc__)


def myprint(dataset, indent=0):
    """Go through all items in the dataset and print them with custom format

    Modelled after Dataset._pretty_str()
    """
    dont_print = ['Pixel Data', 'File Meta Information Version']

    indent_string = "   " * indent
    next_indent_string = "   " * (indent + 1)

    for data_element in dataset:
        if data_element.VR == "SQ":   # a sequence
            print(indent_string, data_element.name)
            for sequence_item in data_element.value:
                myprint(sequence_item, indent + 1)
                print(next_indent_string + "---------")
        else:
            if data_element.name in dont_print:
                print("""<item not printed -- in the "don't print" list>""")
            else:
                repr_value = repr(data_element.value)
                if len(repr_value) > 50:
                    repr_value = repr_value[:50] + "..."
                print("{0:s} {1:s} = {2:s}".format(indent_string,
                                                   data_element.name,
                                                   repr_value))


dcm_path = "/data8/pn/dcm/files/p10/p10999395/s50315575/"
dcm_name = "6948c444-96391ca8-99b4ffc2-b91f9d4e-92529c73"
dcm_ext = ".dcm"
# filename = dcm_path + dcm_name + dcm_ext
filename = '/data8/pn/dcm/files/p10/p10999395/s50315575/a2ab5f78-2b16188c-05dbe86d-8413ad73-1d50bfe8.dcm'
ds = pydicom.dcmread(filename)
myprint(ds)

pocs_val = 'PatientOrientationCodeSequence' in ds
print(f"pocs_val: {pocs_val}")
print(f"len of PatientOrientationCodeSequence: {len(ds.PatientOrientationCodeSequence)}")
cm_not_in_pocs = not ds.PatientOrientationCodeSequence
print(f"cm_not_in_pocs: {cm_not_in_pocs}")

vp_val = 'ViewPosition' in ds
print(f"ViewPosition is in ds: {vp_val}")