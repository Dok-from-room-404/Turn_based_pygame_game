



# Импорт модулей
if __name__ == "__main__":
    from GUI import *
else:
    from .GUI import *
import pickle




class Launcher:
    def read_options(self):
        '''Данный метод получает словарь из файла параметров'''
        input()
        open("launcher\\options.conf")
        input()