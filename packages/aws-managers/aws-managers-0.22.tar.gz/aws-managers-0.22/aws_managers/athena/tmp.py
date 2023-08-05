from aws_managers.athena.columns import IntColumn

int_col = IntColumn('int_col')
print(int_col == 5)

print(int_col.mean())

print(int_col.mean() == 5)
