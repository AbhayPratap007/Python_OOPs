#Python can be used to perform operations on a file.(read & write)

#Type of all files
#1. Text files: .txt, .docx, .log etc.
#2. Binary files: .mp4, .mov, .png, .jpeg etc.

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# 'r'  -  open for reading
# 'w'  -  open for writing, truncating the file first.
# 'x   -  create a new file and open it for writing.
# 'a'  -  open for writing, appending to the end of the file if it exists.
# 'b'  -  binary mode
# 't'  -  text mode
# '+'  -  open a disk file for updating(reading and writing)

# f = open("demo.txt","r")
# data = f.read(5)  #first five letter
# print(data)

# f = open("demo.txt","r")
# line1 = f.readline()  #first line
# print(line1)

# f = open("demo.txt","r")
# line2 = f.readline()  #first line
# print(line2)

# f.close()

# data = f.read()      #read entire line
# data = f.readline()  #read one line at a time

#write to a file
# f = open("demo.txt","w")
#f.write("this is new line")  #overwrites the entire line   #add any file also

# f = open("demo.txt","a")
#f.write("this is new line")  #adds to the line

#delete file
# import os
# os.remove(filename)

#Create a new file "practice.txt" using python. add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like replace programming in Java.

# WAF that replace all occurreneces of "java" with "python" in above file.

# Search if the word "learning" exists in the file or not.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O")
    f.write("using Java\nI like replace programming in Java.")


with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
#----------
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("Find")
    else:
        print("not found") 

