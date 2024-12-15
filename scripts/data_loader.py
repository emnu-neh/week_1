import pandas as pd
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)

        df = df.dropna()
        df = df.drop_duplicates()
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
