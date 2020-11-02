import csv

#write to a new file

#with open('new.csv','w',newline='') as f:
#	writer = csv.writer(f)
#	writer.writerows(['a','b','c'],[4,5,6])

#append to existing file


with open('new.csv','a',newline='') as f:
	writer = csv.writer(f,delimiter=',')
	writer.writerows([['a','b','c'],[4,5,6]])