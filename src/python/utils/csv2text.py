''' This python program should read each line of essays.csv and save it as a separate file with a the name essay<line_number>.txt

That is, the first line should be saved as essay1.txt, the second line as essay2.txt, etc.
'''


filename = r'/Users/sadiyasultana/Desktop/research_files/test_sadiya/test/essays.csv'
f = open(filename)

a =1
line = f.readline()
while line:
    txtfile = open ("essay"+str(a)+".csv", 'w') # saved each line as a file 
    a += 1 # changing the file number
    txtfile.write(line) # writing the line into the new file
    line = f.readline() # moving into the new line
    txtfile.close()

f.close()


 






