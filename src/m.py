import string
filename = "essays.txt"
file_object = open(filename, 'r')
count =0
for line in file_object:
    x = line.translate(string.maketrans("",""), string.punctuation)
    print x
   
