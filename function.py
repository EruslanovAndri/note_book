from datetime import datetime

def createNote():
    id = 0
    title = input("Загаловок: ")
    text = input("Текст: ")
    time = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    return {"ID": id+1,"Title": title,"Text":text,"Time": time}
    
def saveNote():
    pass

def readNote():
    pass

def editNote():
    pass

def deleteNote():
    pass