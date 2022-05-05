# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import mysql.connector
import os
import glob
from functools import partial

#mydb = mysql.connector.connect(
 # host="localhost",
 # user="root",
 # password="Papa1234@"
#)

#path = '/Users/kartiknarula/Downloads/dataverse_files/Files'              
#all_files = glob.glob(os.path.join(path, "*.csv"))

#filepaths = [f for f in os.listdir("/Users/kartiknarula/Downloads/dataverse_files/Files") if f.endswith('.csv')]
p=partial(pd.read_csv, encoding='latin-1')
master_file=pd.concat(map(p, glob.glob("/Users/kartiknarula/Downloads/dataverse_files/Files/*.csv")))
#for file in all_files:
    
 #  file_1989=pd.read_csv("/Users/kartiknarula/Downloads/dataverse_files/1989.csv")
#for f in files
#s=[]
#for i in all_files:
 #   f=pd.read_csv(i, encoding='latin-1')
  #  s.append(f.shape[1])