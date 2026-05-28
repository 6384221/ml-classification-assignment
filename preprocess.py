def preprocess_data(df):
    '''
    Remove missing values and duplicates
    '''
    df_clean = df.dropna().drop_duplicates()

    # Replace spaces in column names
    df_clean.columns = df_clean.columns.str.replace(' ', '_')

    print("Clean Data Shape:", df_clean.shape)

    return df_clean