#First we create the .txt file write some content..
a=open("E:\\PYTHON GUI\DSA PYTHON\\Read.txt","r")

#Print line by line statement

for line in a:
    print(line)
    
a.close()    
#Output the Read text file content
#print(a.read())
# Always close the file, whether an exception occurs or not
#a.close()