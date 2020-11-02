import csv

f = open('find_the_link.csv',encoding= 'utf')
data_csv = csv.reader(f)
data_list = list(data_csv)
link = []
for num in range(len(data_list)):
	link.append(data_list[num][num])
drive_link = ''.join(link)

print(drive_link)
