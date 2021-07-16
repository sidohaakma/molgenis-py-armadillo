import pyarrow.parquet as pq

pq.write_table(df, 'test.parquet')