import os
import glob
import pandas as pd

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/new10-test'

# for f in glob.glob(os.path.join(path, "*.csv")):
#     with open(f, 'r') as csv_file:
#         df = pd.read_csv(csv_file, sep=';')
#         drop_col = [col for col in df.columns if ":" in col]
#         df = df.drop(columns=drop_col)
#     with open(f, 'w') as csv_file:
#         df.to_csv(csv_file, index=False)

def csv_col_drop(csv,cols,sep):

    with open(csv, 'r') as csv_file:
        df = pd.read_csv(csv_file, sep=sep)
    df = df.drop(columns=[col for col in df.columns if col not in cols])
    if not all(df.columns == cols):
        raise KeyError(f"Columns are missing in {csv}")
    with open(csv, 'w') as csv_file:
        df.to_csv(csv_file, index=False)


def csv_checker(path, sep=";"):
    import glob
    import pandas as pd

    table_cols = ['database','cluster','schema','name','description','tags','is_view','description_source']
    col_cols = ['name','description','col_type','sort_order','database','cluster','schema','table_name']
    owner_cols = ['db_name','schema','cluster','table_name','owners']
    stats_cols = ['cluster','db','schema','table_name','col_name','stat_name','stat_val','start_epoch','end_epoch']
    updated_cols = ['cluster','db','schema','table_name','last_updated_time_epoch']

    for f in glob.glob(os.path.join(path, "*.csv")):
        if "table" in f:
            csv_col_drop(f,table_cols, sep)
        
        if "owner" in f:
            csv_col_drop(f,owner_cols, sep)

        if "stats" in f:
            csv_col_drop(f,stats_cols, sep)

        if "col" in f:
            csv_col_drop(f,col_cols, sep)

        if "updated" in f:
            csv_col_drop(f,updated_cols, sep)

csv_checker(path)