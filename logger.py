from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!!')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
                if data_first[i] == '\n' or data_first[i] == '\n\n'or i == len(data_first) - 1:
                    data_first_second.append(''.join(data_first[j:i]))
                    j = i
        data_first = data_first_second
        print(''.join(data_first))



    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())

        print(*data_second)
    
    return data_first, data_second




def put_data():

    data_first, data_second = print_data()  
          
    var = int(input(f"В каком файле изменить данные? "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    n = int(input("Введите номер записи которую нужно изменить: "))
       
    if var == 1:
        while n > len(data_first):
            n = int(input("Такой записи нет. Введите еще раз: "))

    elif var == 2:
        while n > len(data_second) / 2:
            n = int(input("Такой записи нет. Введите еще раз: "))

    input("Введите новые данные ниже")

    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
     
    if var == 1:
        if n - 1 == 0:              
            data_first = [f'{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[n:]
        elif n == len(data_first) :       
            data_first = data_first[:n - 1] + [f'\n{name}\n{surname}\n{phone}\n{adress}\n\n']
        else:
            data_first = data_first[:n - 1] + [f'\n{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[n:]

        with open('data_first_variant.csv', 'w') as file:           
            for i in data_first:
                file.write(i)
        

    else:
        if n - 1 == 0: 
            data_second = [f'{name};{surname};{phone};{adress}\n'] + data_second[2*n - 1:] 
        else:
            data_second = data_second[:2*n - 2] +  [f'{name};{surname};{phone};{adress}\n'] + data_second[2*n - 1:]

                       
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:           
            for i in data_second:
                file.write(f'{i}')

    
    print('Успешно!')
    
      


def delete_data():

    data_first, data_second = print_data()  
         
    var = int(input(f"В каком файле удалить данные? "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    n = int(input("Введите номер записи которую нужно удалить: "))
       
    if var == 1:
        while n > len(data_first):
            n = int(input("Такой записи нет. Введите еще раз: "))

    elif var == 2:
        while n > len(data_second) / 2:
            n = int(input("Такой записи нет. Введите еще раз: "))

    if var == 1:
        if n - 1 == 0:              
            data_first = data_first[n:]
        elif n == len(data_first) :       
            data_first = data_first[:n - 1]
        else:
            data_first = data_first[:n - 1] + data_first[n:]

       
        with open('data_first_variant.csv', 'w') as file:           
            for i in data_first:
                file.write(i)
        

    else:
        if n - 1 == 0: 
            data_second = data_second[2*n:] 
        else:
            data_second = data_second[:2*n - 2] + data_second[2*n:]

                      
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:           
            for i in data_second:
                file.write(f'{i}')

    
    print('Успешно!')
    