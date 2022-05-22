import json
import os


print("Welcome to Login/Signup !")
print("Hello!!\nWould you like to 1.signin and 2.login\nPlease enter 1 if signin and 2 if login.....")
user=input("--->")
d={}
main_dict={}
if user == "1":
    print("Please fill the below requirement for signin...<3")
    name=input("Enter your name: ")
    password=input("Please enter strong password\nEnter your password: ")
    lower=0
    upper=0
    digit=0
    symbol=0
    sum=0
    if len(password)>6:
        for i in password:
            if (i.islower()):
                lower+=1
            if (i.isupper()):
                upper+=1
            if (i.isdigit()):
                digit+=1
            if (i=="@" or i=="$" or i=="#"):
                symbol+=1
        if  (lower>=1 and upper>=1 and digit>=1 and symbol>=1 and lower+upper+digit+symbol==len(password)):
            print("valid password")
        else:
            ("password invalid")
        confirmpassword=input("Enter your password to confirm: ")
        if password ==  confirmpassword:
            print("Password correct\nNow please enter your description below...")
        else:
            print("Your password doesn't match!\nPlease try again...")
        hobby=input("enter your hobby: ")  
        description=input("enter your discription: ") 
        DOB=int(input("enter yor DOB: "))
        gender=input("gender: ")
        d= {}
        l=[]
        d["name"]=name
        d["password"]=confirmpassword
        d['DOB'] = DOB
        d["gender"] = gender
        d['hobby'] = hobby
        d["description"]=description
        l.append(d)
        
        with open("sayjalfile.json","w") as a:
            json.dump(l,a,indent=4)
        print("your are signed up succesfully")
    else:
        print("Please signup again... invalid ...")

else:
    if user == "2":
        print("Please fill your details below...")
        name=input("Enter your name: ")
        password=(input("Enter your password: "))
        with open("sayjalfile.json","r")as a:
            f=a.read()
            if name in f:
                if password in f:
                    print(name ,"your name is exist")
            else:
                hobby=input("enter your hobby: ")  
                description=input("enter your discription: ") 
                DOB=(input("enter yor DOB: "))
                gender=input("gender: ")
                d= {}
                l=[]
                d["name"]=name
                d["password"]=password
                d['DOB'] = DOB
                d["gender"] = gender
                d['hobby'] = hobby
                d["description"]=description 
                l.append(d)
                
                with open("sayjalfile.json","w") as a:
                    f=json.dump(l,a,indent=4)
                    print("congratulation",name ,"you are logen is sucsessfull")       