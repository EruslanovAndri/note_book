import json
import pprint
from function import createNote

def get_path_to_file():
    fileName = '/Users/eruslanovandrey/note_book_project/data.json'
    return fileName

def addToFile(data,fileName):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(fileName, 'a',encoding='UTF-8') as file:
        json.dump(data,file,indent=4)


def readNote(fileName):
    with open(fileName,'r',encoding='UTF-8') as file:
        return json.load(file)
    
# print(readNote(get_path_to_file()))
# input()




# addToFile(createNote(),get_path_to_file())








