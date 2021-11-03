from project_operation import creatp,viewp,deletep,searchp
def projectmenu():
    option = input('plz write c for creat or edit new project,write v for view,write d for delete,write s for search')
    while True:

        option = option.strip()
        if option.isalpha():
            if option == "c":
                creatp()
                break
            elif option == 'v':
                viewp()
                break
            elif option == 'd':
                deletep()
                break
            elif option == 's':
                searchp()
                break