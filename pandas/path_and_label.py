# Choose a single finding and use the results for transfer learning
# This simplifies the problem and requires fewer compute resources
import pandas as pd


JPG_PATH = "data/csv/jpg_file_paths.csv"
META_DATA = "data/csv/mimic-cxr-2.0.0-metadata.csv"
LABEL_PATH = "data/csv/strict_labels.csv"
CSV_PATH = "data/csv/"
HDF_PATH = "data/hdf/"
VIEW_POSITION = 'AP'


# Combines subject_id and study_id to make it easier to join or merge
# dataframes
def combine_subject_study(subject_id, study_id):
    return subject_id * 100_000_000 + study_id


findings = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema',
            'Enlarged_Cardiomediastinum', 'Fracture', 'Lung_Lesion',
            'Lung_Opacity', 'No_Finding', 'Pleural_Effusion',
            'Pleural_Other', 'Pneumonia', 'Pneumothorax', 'Support_Devices']

print(f"findings: {findings}")

jpg_paths = (pd.read_csv(JPG_PATH,
                         usecols=['dicom_id', 'path']
                         )[['dicom_id', 'path']]).set_index(['dicom_id'])
# print(f"df_jpg_paths shape: {jpg_paths.shape}")
# print(f"jpg_paths.head(5): {jpg_paths.head(5)}")
print()

meta_data = (pd.read_csv(META_DATA,
                         usecols=['dicom_id',
                                  'subject_id',
                                  'study_id',
                                  'ViewPosition',
                                  'PatientOrientation']
                         )[['dicom_id',
                            'subject_id',
                            'study_id',
                            'ViewPosition',
                            'PatientOrientation']]).set_index('dicom_id')

# The code below combines subject_id and study_id, making it easier to
# join or merge dataframes
meta_data['subject_study_id'] = combine_subject_study(meta_data['subject_id'],
                                                      meta_data['study_id'])

meta_data = meta_data[(meta_data.ViewPosition == VIEW_POSITION) &
                      (meta_data.PatientOrientation == 'Erect')]
meta_data = meta_data.drop(
    columns=['subject_id', 'study_id', 'ViewPosition', 'PatientOrientation'])
meta_data = meta_data.join(jpg_paths)
# print(f"meta_data shape: {meta_data.shape}")
# print(f"jpg_paths.head(5): {jpg_paths.head(5)}")
# print()

labels = pd.read_csv(LABEL_PATH)


labels['subject_study_id'] = combine_subject_study(labels['subject_id'],
                                                   labels['study_id'])

labels = labels.drop(columns=['subject_id', 'study_id'])


# Remaining labels to keep track of for "for" below

for finding in findings:
    labels_copy = labels.copy()

    print(f"finding: {finding}")
    print(f"labels.copy: {labels_copy.columns}")

    labels_copy = labels_copy.drop(columns=[f for f in labels_copy
                                            if f != finding and
                                            f != 'subject_study_id'])

    print(f"labels_copy after dropping columns: {labels_copy.columns}")
    labels_copy = labels_copy.fillna(0)
    pe = labels_copy[finding]
    labels_copy[finding] = [1 if lbl == 1.0 else 0 for lbl in pe]
    labels_copy = labels_copy.set_index('subject_study_id')

    # print(f"Shape of labels: {labels.shape}")
    # print(f"labels.head(5): {labels.head(5)}")
    # print()
    print(f"Just before meta_data = , labels: {labels_copy.columns}")
    meta_data_copy = meta_data.copy()
    meta_data_copy = meta_data_copy.set_index('subject_study_id')

    data_and_labels = meta_data_copy.join(labels_copy)
    data_and_labels = data_and_labels.set_index('path')
    data_and_labels = data_and_labels.sort_values(by=[finding])

    # For AP, Erect, and Pleural Effusion, there were 3 rows without labels
    data_and_labels = data_and_labels.dropna()
    data_and_labels[finding] = data_and_labels[finding].astype(int)

    """
    print(f"Columns: {data_and_labels.columns}")
    print(f"Unique values: {data_and_labels[finding].unique()}")
    print(f"Value counts: {data_and_labels[finding].value_counts()}")
    print(f"Shape of data_and_labels: {data_and_labels.shape}")
    """

    # Save dataframes to disk
    # Also save to csv for ease of analysis
    data_and_labels.to_hdf(HDF_PATH + finding + '.h5', key='d')
    data_and_labels.to_csv(CSV_PATH + finding + '.csv', index=True)
