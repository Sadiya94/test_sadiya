# this file print the whole text without any punctuation
import string
filename = "essays.txt"
file_object = open(filename, 'r')
txtfile = open ("output.txt", "w") # Sadiya this line here of code creates a new file.

count =0
for line in file_object:
     x = line.translate(string.maketrans("",""), string.punctuation)
     txtfile.write(x) # In this part we are writing the current into our new document.
txtfile.close() # In this last part we are actually closing our file
   
