import os
import create



def checkL(UserData, data):
    os.system('clear')
    print("=====HOME======")
    print("=> Create Quetsion(CQ)")
    print("=> Delate Quetsion(DQ)")
    print("=> Show Quetsion(SQ)")
    i = input("       =>  ")
    j = i.upper()
    match j:
        case "CQ":
            if (UserData['nim'] == data['author']['nim']) and (UserData['P'] == data['author']['P']):
                os.system('clear')
                create.Create()
            else:
                print("you are not a author")
            
        case "DQ":
            os.system('clear')
            print("ini dq")
        case "SQ":
            os.system('clear')
            print("ini sq")