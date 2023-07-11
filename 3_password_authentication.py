import getpass

database = {"syed.hamza": "1234", "hamza.ali": "5678", "ali.shah": "9101"}
user = input("Enter the username : ")
password = getpass.getpass("Enter the password : ")
for i in database.keys():
    if i == user:
        while password != database.get(i):
            password = getpass.getpass("Enter the password Again : ")
print("Verified")
