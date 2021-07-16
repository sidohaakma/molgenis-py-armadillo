import pyarrow as pa
import pyarrow.parquet as pq
import pyreadstat as prs

df, meta = prs.read_sav('/Users/sidohaakma/Documents/Development/Visual/molgenis-py-armadillo/data/lifecycle-fake-data.sav', apply_value_formats=True)
table = pa.Table.from_pandas(df)
pq.write_table(table, 'test.parquet')