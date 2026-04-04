import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Convert Date column (important fix)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove rows where Date is missing
    df = df.dropna(subset=['Date'])

    return df



    # find step 
    