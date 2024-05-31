# пределывает файл в список 
pbk = []
with open("DZ_TELEFON/telefon.py" ,encoding="utf-8" ) as file:                 
    pbk1 = (file.read())
pbk = pbk1.split("\n")
for i in range(0, len(pbk)):
    pbk[i] = pbk[i].split(", ")

for j in range(0, len(pbk)):
    if pbk[j] == [['']]:
        pbk.pop(j)

#Начало работы
def work_with_phonebook():
    choice=show_menu()
    
    while (choice!=7):

        if choice==1:
            print_result(pbk)
        elif choice==2:
            change_phone_book(pbk)
        elif choice==3:
            delit_lem_phone_book(pbk)
        elif choice==4:
            add_lem_phone_book(pbk)
        elif choice==5:
            find_lem_phone_book(pbk)
        elif choice==6:
            phone_book_finhs(pbk,"DZ_TELEFON/telefon.py" )
            break
        choice=show_menu()


#печатает меню
def show_menu():
    print("\n Выбери необходимое действие \n"
        "1. Вывести справочник \n",
        "2. Изменить данные контакта \n",
        "3. Удалить контакт \n",
        "4. Добавить контакт \n",
        "5. Найти контакт \n",
        "6. Закончить работу")
    choice = input()
    if int(choice) <=6 or  not choice == None:
        return int(choice)
    else:
        print("Вы ввели некоректные данные, попробуйте еще раз")
        show_menu()
    

#Вывод контактов
def print_result(a):
    for i in range(0, len(a)):
        b = a[i]
        n = ', '.join(b)
        print(i+1," ." ,n)


#редактирование Контакта        
def change_phone_book(a):
    
    reat = print_menu_change()
    user = user_menu_change(a)
    while(reat !=4):
            if reat == 0 :
                d =a[user]
                name =  input("Введите на что вы хотите изменить фамилию:")
                d[0] = name
                break
            if reat == 1 :
                d =a[user]
                name = input("Введите на что вы хотите изменить Имя:")
                d[1] = name
                break
            if reat == 2 :
                d =a[user]
                name = input("Введите на что вы хотите изменить телефон:")
                d[0] = name
                break 
            if reat == 3 :
                d =a[user]
                name = input("Введите на что вы хотите изменить коментарий:")
                d[0] = name
                break


#Что нужно изменить меню
def print_menu_change():
    
    print("\n Выбери необходимое действие \n"
        "1. Изменить фамилию \n",
        "2. Изменить имя \n",
        "3. Изменить номер \n",
        "4. Изменить коментарий \n")
    reat= (input())
    if int(reat) > 4:
        print("Такой команды не существует, попробуй еще раз")
        print_menu_change()
    return int(reat) -1

#Узнает номер нужного контакта
def user_menu_change(a):
    print_result(a)
    user= (int(input("Введите цифру нужного контакта: ")))-1
    if user  > len(a):
        print("Контакта с таким номером нет")
        user_menu_change(a)
    return user


#удаление контакта
def delit_lem_phone_book(a):
    
    user = user_menu_change(a)
    a =  a.pop(user)

#Добавление нового контакта
def add_lem_phone_book(a):
    fam = input("Введите фамилию нового контакта:")
    user = input("Введите имя нового контакта:")
    nom = input("Введите номер нового контакта:")
    komm = input("Введите коментарий к новому контакту:")
    a.append([fam, user, nom, komm])

#Меню для поиска
def print_menu_find():
    
    print("\n Выбери необхадимое действие \n"
        "1. Искать по фамилии \n",
        "2. Искать по имени \n",
        "3. Искать по номеру \n",
        "4. Искать по коментарию \n")
    reat= input()
    if int(reat) >4 or reat == None:
        print("Вы вели некоректную информацию, попробуйте ещё раз")
        return print_menu_change()
    return int(reat) -1

#Поиск контакта
def find_lem_phone_book(a):
    reat = print_menu_find()
    count = [] 
    while(reat !=4):
           
            if reat == 0 :
                name =  input("Введите фамилию по которой хотите найти контакт:") 
                for i in range(0, len(a)):
                    b = a[i]
                    v = b[0]
                    n = v.lower()
                    srok = name.lower()
                    count.append(is_subseq(srok,  n) )
                for j in range(0, len(a)):
                    if count[j] >= 1:
                        df =a[j]
                        print(*df, sep = ", ")
                break
            if reat == 1 :
                name = input("Введите Имя по которому хотите найти контакт:")
                for i in range(0, len(a)):
                    b = a[i]
                    v = b[1]
                    n = v.lower()
                    srok = name.lower()
                    count.append(is_subseq(srok,  n) )
                for j in range(0, len(a)):
                    if count[j] >= 1:
                        df =a[j]
                        print(*df, sep = ", ")
                break
            if reat == 2 :
                name = input("Введите телефон по которому вы хотите найти контакт:")
                for i in range(0, len(a)):
                    b = a[i]
                    n = b[2] 
                    count.append(is_subseq(name,  n) )
                for j in range(0, len(a)):
                    if count[j] >= 1:
                        df =a[j]
                        print(*df, sep = ", ")
                break 
            if reat == 3 :
                name = input("Введите коментарийи по которому вы хотите найти контакт:")
                for i in range(0, len(a)):
                    b = a[i]
                    v = b[3]
                    n = v.lower()
                    srok = name.lower()
                    count.append(is_subseq(srok,  n) )
                for j in range(0, len(a)):
                    if count[j] >= 1:
                        df =a[j]
                        print(*df, sep = ", ")
                break

#счетчик сходства
def is_subseq(subseq, text):
    count = 0
    for j in range(0,len(subseq)):
        for i in range(0,len(text)):
            if subseq[j] == text[i]:
                count+=1
    return count

#Конец работы
def phone_book_finhs(a, b):
    cv =[]
    with open(b, 'r+') as f:
        file = f
        f.truncate(0)
    with open(b,'w', encoding="utf8") as file:
        for i in range(0, len(a) ):
            c = a[i]
            if i != len(a) - 1:
                c = (', '.join(map(str, c )) + "\n" ) 
            else:
                c = (', '.join(map(str, c )))
            cv.append(c)
        file.writelines(cv)


work_with_phonebook()