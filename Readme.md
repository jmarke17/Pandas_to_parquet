# DataTransformer
A Python class for converting csv files to parquet and json formats.

## Installation
```
pip install pandas
pip install pyarrow
```
## Usage

```
from DataTransformer import DataTransformer

transformer = DataTransformer("data.csv", date_format="%Y-%m-%d %H:%M:%S", delimiter=';')
transformer.read_csv()
transformer.to_parquet("data.parquet", compression='gzip')
transformer.to_json("data.json", date_format="iso")
```
DataTransformer class takes a file path in its constructor and reads the csv file into a pandas dataframe. The class has two methods: to_parquet and to_json which converts the dataframe to parquet and json format respectively and save it to the specified output path using pyarrow for parquet and json for json. The class has new parameters such as date_format and delimiter, this parameters allows the code to handle different formats of the csv entries. Also, the to_parquet method has a new parameter "compression" which allows to compress the data with different algorithms (gzip, snappy, etc).

## Contributing

- Fork it
- Create your feature branch (_git checkout -b my-new-feature_)
- Commit your changes (_git commit -am 'Add some feature'_)
- Push to the branch (_git push origin my-new-feature_)
- Create new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

Special thanks to [PredaZgz](https://github.com/PredaZGZ) for always providing nice ideas.
