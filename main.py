from registration import registration
from login import login
choice=input ('plz write l for login,write r for registration')
while True:

    choice=choice.strip()
    if choice.isalpha():
        if choice=="r":
            registration()
            break
        elif choice=='l':
            login()
            break
