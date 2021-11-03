from project_main_menu import projectmenu
def login():
    list=[]
    x = input("enter your mail")
    y = input("enter your password")
    user = open('users.txt')
    usrloop=user.read()
    for item in usrloop:
        usrdata=usrloop.split()
        print(usrdata)
        if x==usrdata[2] and y==usrdata[3]:
           print ("log sucesse")
           break
    projectmenu()
    user.close()




