import pandas as pd

def data_shape(file_path):
        df=pd.read_csv(file_path)
        return f"Shape of the data {df.shape}"
def main(file_path):
      return data_shape(file_path)
