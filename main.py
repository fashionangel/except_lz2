from err import Cheker


choice = float(input("Выберите номер задания(Всего 1) \n"))
match choice:
    case 1:
        obj = Cheker('var10.csv')    
        obj.catch()