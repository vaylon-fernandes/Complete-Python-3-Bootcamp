import csv

#open csv file 

data = open('example.csv',encoding='utf')
data_csv = csv.reader(data)
data_list = list(data_csv)
emails = []
#list of emails
for row in data_list[1:6]:
	emails.append(row[3])

print('\n',emails,'\n')

#list of full names 
full_name = []
for row in data_list[1:6]:
	full_name.append(row[1]+' '+row[2])
print(full_name)

data.close()