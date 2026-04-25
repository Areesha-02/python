
import os

f=open("file.txt", "w")
f.write("My name is ")
f.close()


f=open("file.txt", "a")
f.write("Areesha")
f.close()


f=open("file.txt", "r")
data = f.read()
print(data)
f.close()
