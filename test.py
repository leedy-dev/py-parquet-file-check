import pyarrow.parquet as pq

# Parquet 파일 경로
file_path = ""

try:
    parquet_file = pq.ParquetFile(file_path)
    print("Parquet 파일이 유효합니다.")
    print("Row Count:", parquet_file.metadata.num_rows)
    print("Column Count:", parquet_file.metadata.num_columns)
    print("Schema:", parquet_file.schema)
except Exception as e:
    print("Parquet 파일에 문제가 있습니다:", e)
