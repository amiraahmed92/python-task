def validation(var):
    while True:
        if var.isalpha()==True:
           # print(var)
            break
        var=input('enter again')


def registration():
    fname=input('plz enter your first name')
    validation(fname)
    lname=input('plz enter your last name')
    validation(lname)
    while True:
      email=input('plz enter your mail')
      if email !="":
      # print(email)
       break
    while True:
        password=input('plz enter your password')
        confirm=input('plz enter your password again')
        if password==confirm:
           # print(password)
            break
    while True:
        phone=input('plz enter your phone')
        if phone[0:2]=="02":
           # print(phone)
            break

    inputstr=" ".join([fname,lname,email,password,phone])
    try:
        new=open("users.txt","a")
    except:
        print ("can not open file")
    else:
        inputstr=inputstr+"\n"
        new.write(inputstr)
        new.close()




