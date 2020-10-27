
import openpyxl
import pandas as pd
import numpy as np
import glob
import os
from pandasgui import show


csvFolder = 'C:\\Users\\tiffa\\OneDrive\\Documents\\!Work\\Cevians\\AMS Calc\\Measurement Data Files\\235_0_S'

csvFiles = glob.glob(os.path.join(csvFolder, '*.csv*'))

combined = []

for file in csvFiles:
    df = pd.read_csv(file)
    df['Source'] = str(file).split('.csv')[0].split('\\')[-1:][0]
    df.drop(['Config Path', 'Config Created', 'Config Modified', 'Integration Time', 'Averaging Nb', 'Smoothing Nb','Spectrometer'], axis=1, inplace = True) 
    combined.append(df)

merged_df = pd.concat(combined)

    ## List all files in directory
        #print(file)

show(merged_df, settings={'block': True})