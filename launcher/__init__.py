



# Импорт модулей
if __name__ == "__main__":
    from GUI import *
else:
    from .GUI import *
import pickle
import sys
import PyQt5
from PyQt5 import QtWidgets




# Класс лаунчера
class Launcher:
    def show(self) -> None:
        '''Данный метод показывает окно лаунчера'''
        options = self.__read_options()
        
        # QtWidgets.QApplication - Создает приложение 
        # QtWidgets.QWidget - Создает окно
        # Создаем приложение с передачей информации о открытых файлов 
        # 1 идет имя скрипта остальное - открытые файлы с помощью скрипта
        self.prog = QtWidgets.QApplication(sys.argv)
        # Создание окна
        self.window = QtWidgets.QMainWindow()

        self.GUI = Ui_MainWindow()
        self.GUI.setupUi(self.window)

        self.window.setWindowTitle("Имя окна")
        # Корректное отображение окна
        self.window.show()
        # Корректное отображение окна
        sys.exit(self.prog.exec())
        

        

    def __read_options(self) -> dict:
        '''Данный метод получает словарь из файла параметров'''
        file = open("launcher\\options.conf", "rb")
        options = pickle.load(file)
        file.close
        return options
        
    def __connect(self) -> None:
        '''Добавляет функции на элементы интерфейса'''
        pass
        
        