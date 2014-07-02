# this file print the whole text without any punctuation
import string
filename = "essays.txt"
file_object = open(filename, 'r')
file = open('output.txt', 'w') # I used this to create a new file

for line in file_object:
    x = line.translate(string.maketrans("",""), string.punctuation)
    file.write(x)# here were are putting the info from the other document
file.close()
   
