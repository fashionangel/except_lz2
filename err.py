import pandas as pd

class Cheker:
    def __init__(self, file_path):
        self.df = file_path

    def catch(self):
        expect_column = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
        expect_dttype = {'Участники гражданского оборота': 'str', 'Тип операции':'str', 'Сумма операции' : 'float64', 'Вид расчета' : 'str', 'Место оплаты' : 'str', 'Терминал оплаты' : 'str', 'Дата оплаты': 'str', 'Время оплаты': 'str', 'Результат операции':'str', 'Cash-back': 'str', 'Сумма cash-back': 'float64'}

        try:
            self.dF = pd.read_csv(self.df)
            col_now = list(self.dF.columns)

            if col_now != expect_column:
                raise KeyError(f'-Названия столбцов не совпадают. \nОжидаемые: {expect_column}\nФактические: {col_now}\n')

            for i,k in expect_dttype.items():
                if i not in col_now:
                    raise TypeError(f"Отсутствует обязательный столбец: '{i}'\n")
                else:
                    type_now = str(self.dF[i].dtypes)
                    if type_now != k:
                        raise TypeError(f"В столбце: '{i}' тип данных не соответствует оиждаемому\nОжидается: {k}, Фактически: {type_now}\n")
                    
        except FileNotFoundError as err:
            print(f'Возникла ошибка следующего типа: {err}')
        except ValueError as err:
            print(f'Возникла ошибка: {err}(Ваш датафрейм пуст)')        
        except TypeError as err:
            print(f"Возникла ошибка: {err} ")
        except KeyError as err:
            print(f"Возникла ошибка структуры данных:\n{err}")
        else:
            print(f'Выполнено успешно')