import sqlite3

def save_to_database(df, db_name='xray_warehouse.db'):
    '''
    Save cleaned data into SQLite database
    '''
    conn = sqlite3.connect(db_name)

    df.to_sql('xray_data', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print(f"Database '{db_name}' created successfully.")