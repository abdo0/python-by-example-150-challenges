import csv

file_read = open('Books.csv', 'r')
for row in file_read:
    print(row)
file_read.close()

start_year = int(input('Enter start year : '))
end_year = int(input('Enter end year : '))

tmp = []
file_read = open('Books.csv', 'r')
file_reader = csv.reader(file_read)
for row in file_reader:
    if start_year < int(row[2]) < end_year:
        print(row)
file_read.close()
