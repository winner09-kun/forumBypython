import json
import os
import check
a = "=====Create Quetsion====="

data = []
folder = 'Quetsion/'
newJoin = []

def newF():
    print("=> input name file")
    global FinalName
    inp = input("  => ") #input for create
    files = os.listdir(folder)
    FinalName = inp.strip()
    
    if f"{FinalName}.json" in files:
        print("This form name already exists")
    else:
        with open(f'Quetsion/{FinalName}.json', 'w') as file:
            json.dump(data, file, indent=4)
        CtaFromNewf()
        
        
    
def CtaFromNewf(): 
    os.system('clear')
    print("input total quetsion")
    TtQuetsion = int(input("  => "))
    while TtQuetsion > 0:
        TtQuetsion -= 1
        CreateQutsion()
        if TtQuetsion == 0:
            SendQuetsion()
            break

def CreateQutsion():
    global newJoin
    Quetsion = input("input Quetsion => ")
    Answer = input("input Answer => ")
    newJoin.append({
        "Question":f"{Quetsion}",
        "Answer":f"{Answer}"
        })

def SendQuetsion():
    print(a)
    i = input("do you want send this form?(y/b) =>")
    if i == "y":
        with open(f'Quetsion/{FinalName}.json', 'w') as file:
            json.dump(newJoin, file, indent=4)
    else:
        print("logout")

def Create():
    print(a)
    print("=> do you want create new quetsion?(y/n)")
    i = input("     =>  ")
    if i == "y":
       os.system('clear')
       print(a)
       newF()
    else:
        check.create()

