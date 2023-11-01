# firstfile=open("first.txt","w")
# open file in append mode
firstfile=open("first.txt","a")

#write content into file
print(" to python programming ",file=firstfile)
firstfile.close();

#open file in read only mode
firstfile=open("first.txt","r")

#read content from the file.
for line in firstfile:
    print(line)

firstfile.close()

