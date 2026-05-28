import pandas as pd

def load_data(file_path):
    '''
    Load CSV dataset into pandas DataFrame
    '''
    df = pd.read_csv(file_path)
    print("Dataset Shape:", df.shape)
    print(df.head())
    return df