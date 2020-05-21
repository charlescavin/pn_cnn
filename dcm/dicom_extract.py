# Coded version of DICOM file '../6610d3f0-93f8fc29-5a82e3ab-8886bb39-b8875605.dcm'
# Produced by pydicom codify utility script
import pydicom
from pydicom.dataset import Dataset
from pydicom.sequence import Sequence

# File meta info data elements
file_meta = Dataset()
file_meta.FileMetaInformationGroupLength = 206
file_meta.FileMetaInformationVersion = b'\x00\x01'
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.1.1'
file_meta.MediaStorageSOPInstanceUID = '2.25.135668630968777895476314079132436052793'
file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
file_meta.ImplementationClassUID = '2.25.55362949469033348352269585565668676650'
file_meta.ImplementationVersionName = 'MIMIC-CXR v2.0.0'

# Main data elements
ds = Dataset()
ds.SpecificCharacterSet = 'ISO_IR 100'
ds.ImageType = ['DERIVED', 'PRIMARY']
ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.1.1'
ds.SOPInstanceUID = '2.25.135668630968777895476314079132436052793'
ds.StudyDate = '21850209'
ds.SeriesDate = '21850209'
ds.AcquisitionDate = '21850209'
ds.ContentDate = '21850209'
ds.StudyTime = '080941.718'
ds.SeriesTime = '080953.859'
ds.AcquisitionTime = '080953.859'
ds.ContentTime = '080953.859'
ds.AccessionNumber = '52257272'
ds.Modality = 'DX'
ds.PresentationIntentType = 'FOR PRESENTATION'
ds.Manufacturer = ''
ds.ReferringPhysicianName = ''

# Procedure Code Sequence
procedure_code_sequence = Sequence()
ds.ProcedureCodeSequence = procedure_code_sequence

# Procedure Code Sequence: Procedure Code 1
procedure_code1 = Dataset()
procedure_code1.CodeValue = 'C11'
procedure_code1.CodingSchemeDesignator = 'CLP'
procedure_code1.CodeMeaning = 'CHEST (PA AND LAT)'
procedure_code_sequence.append(procedure_code1)


# Anatomic Region Sequence
anatomic_region_sequence = Sequence()
ds.AnatomicRegionSequence = anatomic_region_sequence

# Anatomic Region Sequence: Anatomic Region 1
anatomic_region1 = Dataset()
anatomic_region1.CodeValue = 'T-D3000'
anatomic_region1.CodingSchemeDesignator = 'SNM3'
anatomic_region1.CodeMeaning = 'Chest'
anatomic_region1.MappingResource = 'DCMR'
anatomic_region1.ContextGroupVersion = '20020904'
anatomic_region1.ContextIdentifier = '4031'
anatomic_region_sequence.append(anatomic_region1)

ds.PatientName = ''
ds.PatientID = '10999512'
ds.PatientBirthDate = ''
ds.PatientSex = ''
ds.PatientIdentityRemoved = 'YES'
ds.DeidentificationMethod = 'Basic Prof. PS3.15 Table E.1-1 2017e, with options.'

# De-identification Method Code Sequence
deidentification_method_code_sequence = Sequence()
ds.DeidentificationMethodCodeSequence = deidentification_method_code_sequence

# De-identification Method Code Sequence: De-identification Method Code 1
deidentification_method_code1 = Dataset()
deidentification_method_code1.CodeValue = '113100'
deidentification_method_code1.CodingSchemeDesignator = 'DCM'
deidentification_method_code1.CodingSchemeVersion = '20170914'
deidentification_method_code1.CodeMeaning = 'Basic Application Confidentiality Profile'
deidentification_method_code_sequence.append(deidentification_method_code1)

# De-identification Method Code Sequence: De-identification Method Code 2
deidentification_method_code2 = Dataset()
deidentification_method_code2.CodeValue = '113105'
deidentification_method_code2.CodingSchemeDesignator = 'DCM'
deidentification_method_code2.CodingSchemeVersion = '20170914'
deidentification_method_code2.CodeMeaning = 'Clean Descriptors Option'
deidentification_method_code_sequence.append(deidentification_method_code2)

# De-identification Method Code Sequence: De-identification Method Code 3
deidentification_method_code3 = Dataset()
deidentification_method_code3.CodeValue = '113107'
deidentification_method_code3.CodingSchemeDesignator = 'DCM'
deidentification_method_code3.CodingSchemeVersion = '20170914'
deidentification_method_code3.CodeMeaning = 'Retain Longitudinal Temporal Information Modified Dates Option'
deidentification_method_code_sequence.append(deidentification_method_code3)

# De-identification Method Code Sequence: De-identification Method Code 4
deidentification_method_code4 = Dataset()
deidentification_method_code4.CodeValue = '113101'
deidentification_method_code4.CodingSchemeDesignator = 'DCM'
deidentification_method_code4.CodingSchemeVersion = '20170914'
deidentification_method_code4.CodeMeaning = 'Clean Pixel Data Option'
deidentification_method_code_sequence.append(deidentification_method_code4)

# De-identification Method Code Sequence: De-identification Method Code 5
deidentification_method_code5 = Dataset()
deidentification_method_code5.CodeValue = '113103'
deidentification_method_code5.CodingSchemeDesignator = 'DCM'
deidentification_method_code5.CodingSchemeVersion = '20170914'
deidentification_method_code5.CodeMeaning = 'Clean Graphics Option'
deidentification_method_code_sequence.append(deidentification_method_code5)

ds.BodyPartExamined = 'CHEST'
ds.KVP = "110.0"
ds.DistanceSourceToDetector = "1846.0"
ds.TableType = 'FIXED'
ds.FieldOfViewShape = 'RECTANGLE'
ds.FieldOfViewDimensions = [424, 353]
ds.ExposureTime = "27"
ds.XRayTubeCurrent = "125"
ds.Exposure = "3"
ds.ExposureInuAs = "3300"
ds.RectificationType = 'THREE PHASE'
ds.ImageAndFluoroscopyAreaDoseProduct = "1.572"
ds.FilterType = 'NONE'
ds.ImagerPixelSpacing = [0.139, 0.139]
ds.Grid = 'NONE'
ds.AnodeTargetMaterial = 'TUNGSTEN'
ds.RelativeXRayExposure = "1419"
ds.ExposureIndex = "181.3"
ds.TargetExposureIndex = "249.48"
ds.DeviationIndex = "-1.39"
ds.PositionerType = 'RIGID'
ds.CollimatorShape = 'RECTANGULAR'
ds.CollimatorLeftVerticalEdge = "4"
ds.CollimatorRightVerticalEdge = "2544"
ds.CollimatorUpperHorizontalEdge = "0"
ds.CollimatorLowerHorizontalEdge = "3052"
ds.ViewPosition = 'PA'
ds.Sensitivity = "1039.0"
ds.DetectorTemperature = "27.0"
ds.DetectorType = 'DIRECT'
ds.DetectorConfiguration = 'AREA'
ds.DetectorBinning = [1, 1]
ds.DetectorElementPhysicalSize = [0.139, 0.139]
ds.DetectorElementSpacing = [0.139, 0.139]
ds.ExposureControlMode = 'AUTOMATIC'
ds.ExposureControlModeDescription = 'L,R/5'
ds.StudyInstanceUID = '2.25.126188518033689857013135429659842351432'
ds.SeriesInstanceUID = '2.25.240092234409214761483667705096777941684'
ds.StudyID = '52257272'
ds.SeriesNumber = "1"
ds.AcquisitionNumber = "1"
ds.InstanceNumber = "1"
ds.PatientOrientation = ['R', 'F']
ds.ImageLaterality = 'U'
ds.ImagesInAcquisition = "1"
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = 'MONOCHROME2'
ds.Rows = 3056
ds.Columns = 2544
ds.PixelSpacing = [0.139, 0.139]
ds.BitsAllocated = 16
ds.BitsStored = 12
ds.HighBit = 11
ds.PixelRepresentation = 0
ds.SmallestImagePixelValue = 0
ds.LargestImagePixelValue = 4095
ds.BurnedInAnnotation = 'NO'
ds.PixelIntensityRelationship = 'LOG'
ds.PixelIntensityRelationshipSign = -1
ds.WindowCenter = "2048.0"
ds.WindowWidth = "4096.0"
ds.RescaleIntercept = "0.0"
ds.RescaleSlope = "1.0"
ds.RescaleType = 'US'
ds.LossyImageCompression = '00'
ds.RequestingService = 'EU'
ds.PerformedProcedureStepStartDate = '21850209'
ds.PerformedProcedureStepStartTime = '080941.718'
ds.PerformedProcedureStepDescription = 'CHEST (PA AND LAT)'
ds.ExposedArea = [42, 35]

# View Code Sequence
view_code_sequence = Sequence()
ds.ViewCodeSequence = view_code_sequence

# View Code Sequence: View Code 1
view_code1 = Dataset()
view_code1.CodeValue = 'R-10214'
view_code1.CodingSchemeDesignator = 'SNM3'
view_code1.CodeMeaning = 'postero-anterior'
view_code1.MappingResource = 'DCMR'
view_code1.ContextGroupVersion = '20040302'
view_code1.ContextIdentifier = '4010'
view_code_sequence.append(view_code1)


# Patient Orientation Code Sequence
patient_orientation_code_sequence = Sequence()
ds.PatientOrientationCodeSequence = patient_orientation_code_sequence

# Patient Orientation Code Sequence: Patient Orientation Code 1
patient_orientation_code1 = Dataset()
patient_orientation_code1.CodeValue = 'F-10440'
patient_orientation_code1.CodingSchemeDesignator = 'SNM3'
patient_orientation_code1.CodeMeaning = 'Erect'
patient_orientation_code1.MappingResource = 'DCMR'
patient_orientation_code1.ContextGroupVersion = '20020904'
patient_orientation_code1.ContextIdentifier = '19'
patient_orientation_code_sequence.append(patient_orientation_code1)


# Graphic Annotation Sequence
graphic_annotation_sequence = Sequence()
ds.GraphicAnnotationSequence = graphic_annotation_sequence

# Graphic Annotation Sequence: Graphic Annotation 1
graphic_annotation1 = Dataset()

# Referenced Image Sequence
refd_image_sequence = Sequence()
graphic_annotation1.ReferencedImageSequence = refd_image_sequence

# Referenced Image Sequence: Referenced Image 1
refd_image1 = Dataset()
refd_image1.ReferencedSOPClassUID = '1.2.840.10008.5.1.4.1.1.1.1'
refd_image1.ReferencedSOPInstanceUID = '2.25.135668630968777895476314079132436052793'
refd_image_sequence.append(refd_image1)


# Graphic Object Sequence
graphic_object_sequence = Sequence()
graphic_annotation1.GraphicObjectSequence = graphic_object_sequence
graphic_annotation_sequence.append(graphic_annotation1)

ds.PresentationLUTShape = 'IDENTITY'
ds.PixelData = # XXX Array of 15548928 bytes excluded

ds.file_meta = file_meta
ds.is_implicit_VR = False
ds.is_little_endian = True
ds.save_as(r'test.dcm', write_like_original=False)