import os

'''email = ("oludvav")
country = ("usa")
print("your email is "+ email + " and country " + country)

if email =="" or country =="":
    print("please fill email and country")

elif email !="" and country !="":
    print("succesful")

myFile= open("indext.html", "r")
x = myFile.readlines()
for y in x:
    print(y)
myFile.close()'''

nameoffile = input("Enter your file name")
writein = input("Enter content")
x = open(nameoffile,"w")
x.write(writein)
print("success")
query = input("yes or no")
if query == "yes":
    print("session continue")
elif query == "no":
    os.remove(nameoffile)
else:
    print("try again")
x.close()

'''x=2
y=3
z=x+y
print(z)'''
