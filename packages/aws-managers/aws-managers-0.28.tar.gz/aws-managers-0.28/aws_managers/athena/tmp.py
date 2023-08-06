from aws_managers.athena.queries import IntegerColumnQuery

int_col = IntegerColumnQuery('int_col')
print(int_col == 5)

print(int_col.mean())

print(int_col.mean() == 5)
