import os
import glob
import pandas as pd

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/new10'

for f in glob.glob(os.path.join(path, "*.csv")):
    with open(f, 'r') as csv_file:
        df = pd.read_csv(csv_file, sep=';')
        drop_col = [col for col in df.columns if ":" in col]
        df = df.drop(columns=drop_col)
    with open(f, 'w') as csv_file:
        df.to_csv(csv_file, index=False)