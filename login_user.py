import soal
import json

with open('user.json', 'r') as file:
    data = json.load(file)  

# sistem login
def login():
    Nim = input("Masukan Nim anda: ")
    passw = input("Masukan Password: ")
    if Nim != data['author']['nim']:
        print("Nim anda salah")
    elif passw != data['author']['P']:
        print("Password anda salah")
    else:
        print("Anda berhasil login")
        soal.check()
login()