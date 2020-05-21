# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
# license : MIT

from __future__ import print_function

import pydicom


def myprint(dataset, indent=0):
    """Go through all items in the dataset and print them with custom format

    Modelled after Dataset._pretty_str()
    """
    dont_print = ['Pixel Data', 'File Meta Information Version']

    indent_string = "   " * indent
    next_indent_string = "   " * (indent + 1)

    for data_element in dataset:
        if data_element.VR == "SQ":   # a sequence
            print(indent_string, "SEQ", data_element.name)
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

filename = "/Users/cc/Documents/_Current/Dev/AI/Physio.org/Dicom_Files/s50414267/02aa804e-bde0afdd-112c0b34-7bc16630-4e384014.dcm"
ds = pydicom.dcmread(filename)

myprint(ds)