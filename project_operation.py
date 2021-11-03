import datetime
def creatp():
    while True:
        title = input(" plz enter Title : ")
        if title != "":
             break
    while True:
        details = input("plz enter Details : ")
        if details != "":
             break
    while True:
        total_target = input("plz enter Total target : ")
        t=int(total_target)
        if t <= 250000:
             break

    while True:
        start_time = input("plz enter Start Date  : ")
       # end_time = input("plz enter End Date : ")

        day, month, year = start_time.split('/')

        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate):
            break
    while True:
        end_time = input("plz enter End Date : ")

        day, month, year = end_time.split('/')

        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate):
            break




    inputpro = ":".join([title, details, total_target, start_time, end_time])
    try:
        newpro = open("project1.txt", "a")
    except:
        print("can not open file")
    else:
        inputpro = inputpro + "\n"
        newpro.write(inputpro)
        newpro.close()
def viewp():
    project = open('project1.txt')
    projectloop = project.readlines()
    print(projectloop)

def update():
    project_namee = input('plz enter project name')
    change=input('plz enter what you want to change')
    newchange=input('plz enter new value')
    project = open('project1.txt')
    projectloop = project.readlines()
    print(projectloop)
    projects = []
    for line in projectloop:
        projects.append(line.strip("\n"))
    for item in projects:
        project_data = item.split(":")
        if project_data[0] == project_namee:
            print(project_data)
            f = open('project1.txt', 'w')
            for i in  range(len(project_data)):
                if project_data[i]==change:
                   project_data[i]=newchange
                   print(project_data)

def deletep():
    project_name=input('plz enter project name')
    project = open('project1.txt')
    projectloop = project.readlines()
    print(projectloop)
    projects=[]
    for line in projectloop:
        projects.append(line.strip("\n"))
    for item in projects:
        project_data=item.split(":")
        if project_data[0]==project_name:
            print(project_data)
            projects.remove(item)
            print(projects)
            f=open('project1.txt','w')
            for i in projects:
                data=i+"\n"
                f.write(data)



def searchp():
    project_start = input('plz enter project start date')
    project_end = input('plz enter project end date')
    project = open('project1.txt')
    projectloop = project.readlines()
    #print(projectloop)
    projects = []
    for line in projectloop:
        projects.append(line.strip("\n"))
    for item in projects:
        project_data = item.split(":")
        if project_data[3] == project_start and project_data[4]==project_end:
            print(project_data)

