import csv


# --------- READING CSV ----------

# 1 - Built-in CSV Library
# here return an array --> ['John Smith', 'Accounting', 'November']

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    count = 0
    for row in csv_reader:
        print(row)
        # if count == 0:
        #     print(f'Columns are {", ".join(row)}')
        #     count += 1
        # else:
        #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #     count += 1
    print(f'Processed {count} lines.')


# 2 - Reading CSV Files Into a Dictionary
# return dictionary of arrays --> [('name', 'John Smith'), ('department', 'Accounting'), ('birthday month', 'November')]

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for row in csv_reader:
        print(row)
        # if count == 0:
        #     print(f'Column names are {", ".join(row)}')
        #     count += 1
        # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        # count += 1
    print(f'Processed {count} lines.')



# --------- WRITING CSV ----------

# 1 - Built-in CSV Library

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# 2 - Reading CSV Files Into a Dictionary

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
