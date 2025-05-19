import pandas as pd
import numpy as np

df=pd.read_csv(r"/Users/praneelchetlapalli/Downloads/cereal.csv")
selectedcols=["Protein (g)","Fat","Sodium","Dietary Fiber","Carbs","Sugars","Display Shelf","Potassium"	,"Vitamins and Minerals"]
numericdf=df[selectedcols]
for cols in numericdf.coloumns:
    mean = numericdf[cols]