filename = "essays.txt"
file_object = open(filename, 'r')
count = 0
x = file_object.readline()
while x:
	count = count + 1
	x = file_object.readline()

print count
