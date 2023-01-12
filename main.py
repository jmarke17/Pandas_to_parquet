import pandas as pd
import pyarrow
import json

class DataTransformer:
    def __init__(self, file_path, date_format=None, delimiter=','):
        self.file_path = file_path
        self.dataframe = None
        self.date_format = date_format
        self.delimiter = delimiter

    def read_csv(self):
        """
        Read csv file into a pandas dataframe.
        """
        self.dataframe = pd.read_csv(self.file_path, delimiter=self.delimiter, parse_dates=True, infer_datetime_format=True)
        if self.date_format:
            self.dataframe = self.dataframe.apply(lambda x: pd.to_datetime(x, format=self.date_format) if x.dtype == "datetime64[ns]" else x)
    
    def to_parquet(self, output_path, compression='snappy'):
        """
        Convert the data to a parquet format and save it to the specified output path.
        """
        table = pyarrow.Table.from_pandas(self.dataframe)
        pyarrow.parquet.write_table(table, output_path, compression=compression)
        print(f"Data saved to {output_path} in parquet format with compression {compression}.")

    def to_json(self, output_path, date_format=None):
        """
        Convert the data to a json format and save it to the specified output path.
        """
        json_str = self.dataframe.to_json(date_format=date_format)
        with open(output_path, 'w') as outfile:
            json.dump(json_str, outfile)
        print(f"Data saved to {output_path} in json format.")

# Example usage
transformer = DataTransformer("data.csv", date_format="%Y-%m-%d %H:%M:%S", delimiter=';')
transformer.read_csv()
transformer.to_parquet("data.parquet", compression='gzip')
transformer.to_json("data.json", date_format="iso")