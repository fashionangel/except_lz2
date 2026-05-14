from err_catch import Opener


choice = int(input("Выберите номер задания(у нас : 1) \n"))
match choice:
    case 1:
        obj = Opener('var10.csv')    
        obj.catcher()