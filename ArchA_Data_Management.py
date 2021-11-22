#import all the libraries

import io
import pandas as pd
import glob
from tabulate import tabulate

#function definations
############ Create a function which reads from a directory and return table with Mipox parameters and lot and wafer ID.
def read_excel_files(directory,sheetName,fileName):
    all_data = pd.DataFrame()
    data = pd.DataFrame()
    directory = directory+ fileName +".xlsx"


    for f in glob.glob(directory):
        print(f)
        #data = pd.read_excel(f, header=[2],sheet_name=sheetName)
        data = pd.read_excel(f, header=[0], sheet_name=sheetName)
        #print(tabulate(data))
        all_data = pd.concat([all_data, data],ignore_index=True)
    return all_data

#directory = "C:\\Users\senguel\OneDrive - Facebook\Architecture A\Process Tracker\EVG Bonding Process Tracker Files"
directory = "C:\\Users\senguel\PycharmProjects\python-intro\Venv"
fileName = "\ArchA_Led"
sheet_name = "Sheet1"
data1 = read_excel_files(directory,sheet_name, fileName)

fileName = "\ArchA_Process"
sheet_name = "Sheet1"
data2 = read_excel_files(directory,sheet_name, fileName)
result = pd.merge(data1, data2, on=None, left_on='EVG_wafer_id',right_on='wafer_id_top')

result.to_excel("ArchA_Merged.xlsx")

print ("These Changes are for checking compare and pull request")
