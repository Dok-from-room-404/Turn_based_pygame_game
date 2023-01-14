



import random
import pickle
import sys



simvol_floor = [".", ",", "/"]
simvol_obstacles = ["#", "$"]
simvol_wall = [":", ";"]
simvol_player = "@"
simvol_save_point = "s"

simvoles = [".", ",", "/", "#", "$", ":", ";", "@", "s"]


class Map:
    '''Класс уровня'''
    def __init__(self):
        '''Инициализирует класс и создает список для строчек уровня'''
        self.list = []
        # Количество актеров (Всего возможно только 1 за весь уровень) False - количество = 0
        self.flag_actor = False
        # Количество save_point (Всего возможно только 1 за весь уровень) False - количество = 0
        self.flag_save_point = False
        # Длина чстрочки для уровня
        self.len_level = None
        
    def get_flag(self) -> tuple:
        '''Возвращает кортеж из flag_actor, flag_save_point'''
        return self.flag_actor, self.flag_save_point
    
    def append_string(self, level_string:str):
        '''Добавляет к уровню строку '''
        if len(level_string) != self.len_level and self.len_level != None:
            print("Строчка имеет не правильную длину. Данная строка отклонена")
            return 


        if simvol_player in level_string:
            if self.flag_actor:
                # Если актер уже был добавлен и он есть в строке
                print("Актер уже был добавлен. Данная строка отклонена")
                return
            elif level_string.count(simvol_player) > 1:
                # Если количество актеров более 1 в строке
                print("Более одного актера в строке. Данная строка отклонена")
                return
            else:
                self.flag_actor = True
            
            
        if simvol_save_point in level_string:  
            if self.flag_save_point:
                print("Точка сохранения уже была добавлена. Данная строка отклонена")
                return
            elif level_string.count(simvol_save_point) > 1:
                print("Более одной точки сохранения в строке. Данная строка отклонена")
                return
            else:
                self.flag_save_point = True
            
        sp_string_level = []
        for i in level_string:
            if i not in simvoles:
                print("Данный символ \'{0}\' нельзя использовать в уровне. Данная строка отклонена".format(str(i)))
                return 
            else:
                sp_string_level.append(i)
        else:
            print("Данная строка записана ")
            self.len_level = len(level_string)
            self.list.append(sp_string_level)
            
    def get_map(self) -> list:
        '''Возвращает карту'''
        return self.list 
            


class Writer:
    '''Класс для записи уровней в файл'''
    def __init__(self, roat_file:str) -> None:
        '''Инициализирует класс и открывает файл в режиме перезаписи'''
        try:
            file = open(roat_file, "rb")
            self.old_inform = pickle.load(file)
            print(self.old_inform)
            file.close()
        except:
            self.old_inform = {}
        self.file = open(roat_file, "wb")
        # Список уровней
        self.list_level = []
        
    def append(self, maper:Map)-> None:
        if all(maper.get_flag()):
            self.list_level.append(maper.get_map())
        else:
            print("На карте отсутствует герой или точка сохранения. Уровень не добавлен")
            print("Уровень")
            for i in maper.get_map():
                print(i) 
        print("Уровни")
        for i in self.list_level:
            print(i)
            
    def save(self):
        pickle.dump(self.list_level, self.file)
        self.file.close()
        




# Список уровней (каждый уровень представляет список)
lvl1 = [["/", "/"],
        ["@", "s"]]


list_levels = [lvl1]


if __name__ == "__main__":
    if len(list_levels) == 0:
        # Уровни
        levels = Writer("levels.levl")
        print("Желаете ли вы добавить уровень: \n1 – Да \n2 - Конец запроса уровней")
        for i in sys.stdin:
            if i.strip() == "1":
                level = Map()
                print()
                print("Желаете ли вы добавить строчку к уровню : \n1 – Да \n2 - Конец строчек к уровню")
                for ii in sys.stdin:   
                    if ii.strip() == "1":
                        level.append_string(input("Введите строчку уровня\n"))
                        print("Карта уровня")
                        print(level.get_map())
                        
                    elif ii.strip() == "2":
                        levels.append(level)
                        break
                    else:
                        print("Неправильный ввод !")
                    print()
                    print("Желаете ли вы добавить строчку к уровню : \n1 – Да \n2 - Конец строчек к уровню")

            elif i.strip() == "2":
                levels.save()
                break
            else:
                print("Неправильный ввод !")
            print()
            print("Желаете ли вы добавить уровень: \n1 – Да \n2 - Конец запроса уровней")
    else:
        file = open("levels.levl", "wb")
        pickle.dump(list_levels, file)
        file.close()
        with open("levels.levl", 'rb') as f:
            print(pickle.load(f))
    
