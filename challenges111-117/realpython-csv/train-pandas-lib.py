import pandas

# --------- READING CSV ----------

df = pandas.read_csv('hrdata.csv')
print(df)


df = pandas.read_csv('hrdata.csv', index_col='Name')
print(df)


df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)


dfNh = pandas.read_csv('hrdata-noheader.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(dfNh)


# --------- WRITING CSV ----------

df = pandas.read_csv('hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')
