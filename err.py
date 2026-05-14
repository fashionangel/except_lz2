import pandas as pd

class Opener:
    def __init__(self, file_path):
        self.df = file_path

    def catcher(self):
        expected_col = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
        expected_dtypes = {'Участники гражданского оборота': 'str', 'Тип операции':'str', 'Сумма операции' : 'float64', 'Вид расчета' : 'str', 'Место оплаты' : 'str', 'Терминал оплаты' : 'str', 'Дата оплаты': 'str', 'Время оплаты': 'str', 'Результат операции':'str', 'Cash-back': 'str', 'Сумма cash-back': 'float64'}

        try:
            self.dF = pd.read_csv(self.df)
            col_now = list(self.dF.columns)

            if col_now != expected_col:
                raise KeyError(f'-Названия столбцов не совпадают. \nОжидаемые: {expected_col}\nФактические: {col_now}\n')

            for i,j in expected_dtypes.items():
                if i not in col_now:
                    raise TypeError(f"Отсутствует обязательный столбец: '{i}'\n")
                else:
                    type_now = str(self.dF[i].dtypes)
                    if type_now != j:
                        raise TypeError(f"В столбце: '{i}' тип данных не соответствует оиждаемому\nОжидается: {j}, Фактически: {type_now}\n")
                    
        except FileNotFoundError as e:
            print(f'Возникла ошибка следующего типа: {e}')
        except ValueError as e:
            print(f'Возникла ошибка: {e}(Ваш датафрейм пуст)')        
        except TypeError as e:
            print(f"Возникла ошибка: {e} ")
        except KeyError as e:
            print(f"Возникла ошибка структуры данных:\n{e}")
        else:
            print(f'Чтение завершено успешно')