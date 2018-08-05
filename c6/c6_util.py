import pandas as pd


def read_showcases(file_name):
    df_data = pd.read_csv(file_name)
    df_data.dropna(inplace=True)
    df_data.set_index(df_data.columns[0], inplace=True)
    df_data = df_data.astype(float)
    df_data = df_data.T
    df_data.columns.name = None
    return df_data
