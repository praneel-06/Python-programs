import pandas as pd
import numpy as np

df = pd.read_csv(r"/Users/praneelchetlapalli/Downloads/cereal.csv")
numeric_df = df.select_dtypes(include=("number"))
summary = numeric_df.describe().loc[["min","25%","50%","75%","max"]]
print (summary)

