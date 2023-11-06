#open the file
firstfile=open("fms.txt","a")

#write data into file
print("programming ",file=firstfile)

#close the file
firstfile.close()


#open the file in read only mode
firstfile=open("fms.txt","r")

# for line in firstfile:
#     print(line)

print(firstfile.read())
#close the file
firstfile.close()


