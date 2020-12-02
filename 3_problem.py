documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def name_from_number():
  number = input("Напишите номер документа")
  is_found = False
  for doc in documents:
    if doc["number"] == number:
      name = doc["name"]
      print(name)
      is_found = True
      break
  if is_found == False:
    print("Вы ввели неправильный номер - в списке наших документов нет документа с таким номером. Вас сейчас выведет в главное меню, можете попробовать снова")

def shelf_from_number():
  number = input("Напишите номер документа")
  is_found = False
  for shelf in directories.items():
    if shelf[1].count(number) == 1:
      searched_shelf = shelf[0]
      print(searched_shelf)
      is_found = True
      break
  if is_found == False:
    print("Вы ввели неправильный номер - на наших полках нет документа с таким номером. Вас сейчас выведет в главное меню, можете попробовать снова")

def show_all_docs():
  for doc in documents:
    print(doc["type"], f'"{doc["number"]}" "{doc["name"]}"')

def add_document():
  number = input("Напишите, пожалуйста, идентификационный номер добавляемого документа")
  type = input("Напишите, пожалуйста, к какому типа принадлежит добавляемый документ")
  name = input("Напишите, пожалуйста, имя владельца добавляемого документа")
  shelf = input("Напишите, пожалуйста, на какую полку вы хотите добавить документ")

  shelves = []
  for element in directories.keys():
    shelves.append(element)

  
  while True:
    if directories.get(shelf) != None:
      new_doc = {"type" : type, "number" : number, "name" : name}
      documents.append(new_doc)
      directories[shelf].append(number)
      print("Ваш документ добавлен")
      break
    else:
      print(f"Вы указали несуществующую полку. Пожалуйста, укажите существующую полку. На данный момент у нас есть полки под номерами {shelves}")
      decision = input('Попробуете ввести еще раз или решили отказаться от выполнения данной команды? Ответьте "yes" или "no"')
      if decision == "yes":
        shelf = input("Напишите, пожалуйста, на какую полку вы хотите добавить или переместить документ")
      else:
        break

def delete_document():
  number = input("Укажите номер документа, который хотите удалить")
  document_is_correct = False
  for doc in documents:
    if doc["number"] == number:
      document_is_correct = True
      documents.remove(doc)
      for value in directories.values():
        if value.count(number) == 1:
          value.remove(number)
          print("Документ удален")
          break
  


  if document_is_correct == False:
    print("Вы ввели неправильный номер - в списке наших документов нет документа с таким номером. Вас сейчас выведет в главное меню, можете попробовать снова")

def move_document():
  number = input("Напишите, пожалуйста, номер документа, который Вы хотите переместить на другую полку")

  document_is_correct = False
  for doc in documents:
    if doc["number"] == number:
      document_is_correct = True
  
  if document_is_correct == False:
    print("Вы ввели неправильный номер - в списке наших документов нет документа с таким номером. Вас сейчас выведет в главное меню, можете попробовать снова")

  else:
    shelf = input("Напишите, пожалуйста, на какую полку вы хотите добавить документ")

    shelves = []
    for element in directories.keys():
      shelves.append(element)
    
    while True:
      if directories.get(shelf) != None:
        directories[shelf].append(number)
        print("Ваш документ перенесен")
        break
      else:
        print(f"Вы указали несуществующую полку. Пожалуйста, укажите существующую полку. На данный момент у нас есть полки под номерами {shelves}")
        decision = input('Попробуете ввести еще раз или Вы решили отказаться от выполнения данной команды? Ответьте "yes" или "no"')
        if decision == "yes":
          shelf = input("Напишите, пожалуйста, на какую полку вы хотите добавить или переместить документ")
        else:
          break

def add_shelf():
  new_shelf = input("Под каким номером вы хотите добавить полку?")

  shelves = []
  for element in directories.keys():
    shelves.append(element)

  while directories.get(new_shelf) != None:
    print(f"Вы указали существующую полку. Пожалуйста, укажите несуществующую полку. На данный момент у нас есть полки под номерами {shelves}")
    new_shelf = input("Напишите, пожалуйста, на какую полку вы хотите перенести документ")
  
  directories[new_shelf] = []

def commands_list():
  
  print("'p' - Узнать имя человека, зная номер документа.")
  print("'s' - Узнать номер полки, зная номер документа, тогда введите команду .")
  print("'l' - Увидеть список всех документов.")
  print("'a' - Добавить документ на определенную полку.")
  print("'d' - Удалить документ из перечня документов и с полки.")
  print("'m' - Перенести документ с одной полки на другую.")
  print("'as' - Добавить новую полку.")
  print("'c' - Увидеть список всех команд.")
  print("'n' - Показать список имен всех владельцев документов")



def names_list():
  try:
   for document in documents:
     print(document["name"])
  except KeyError:
    print("У документа номер '", document["number"], "' нет поля 'name'. Пожалуйста, заполните поле 'name' у этого документа")




def main():
  print("Здраствуйте, уважаемый пользователь. Сейчас я покажу Вам список команд, которые вы можете использовать:")
  commands_list()
  
  while True:
    order = input("Какую команду Вы хотите использовать?")
    if order == "p":
      name_from_number()
    elif order == "s":
      shelf_from_number()
    elif order == "l":
      show_all_docs()
    elif order == "a":
      add_document()
    elif order == "d":
      delete_document()
    elif order == "m":
      move_document()
    elif order == "as":
      add_shelf()
    elif order == "c":
      commands_list()
    elif order == "n":
      names_list()

main()
