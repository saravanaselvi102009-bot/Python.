f=open('CSE_SecA.txt','w')
f.write("This is My first file")
f.close()

f = open('CSE_SecA.txt','r')
print(f.read())
f.close()

f=open("SAN_CSE","w")
f.writelines(["a\n", "b\n", "c\n)"])
f.close()

f=open("SAN_CSE","r")
print(f.read())
f.close()

import.OS
if OS.path.exists
print(file.exists)