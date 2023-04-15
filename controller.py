from function import createNote
from database import addToFile, get_path_to_file,readNote


def data_operations(): # позволяет выбрать между вариантами редактирования записной книги.
    while True:
        choice = input("Выберите команду: ")
        if choice == "1": # Добавляет новую запись в notebook.
                addToFile(createNote(),get_path_to_file()) # work 
        elif choice == "2": # чтение файла 
                print(readNote(get_path_to_file()))
        elif choice == "3":
              break

data_operations()