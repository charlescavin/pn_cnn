import pandas as pd


df = pd.read_csv("/home/cc/dev/cv/pn/data/csv_files/pn_jpg_data2.csv")
df.drop(columns=["Num2"])
df.to_csv("/home/cc/dev/cv/pn/data/csv_files/pn_jpg_data3.csv")
