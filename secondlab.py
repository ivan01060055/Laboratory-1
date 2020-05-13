data={}
flag = True 
Z  = r'file.txt'
with open(Z , 'r') as file:
    for line in file:
        if line[0] != "#" and line[0] !=';' and line[0] != '\n':
            list0 = line.split(' ')
            f=len(list0)
                
                
        
            
            if f == 2:
                key = list0[0]
                value = list0[1]
                data[key]= value
            elif f == 1:
                key = list0[0].rstrip('\n')
                value = "Значение у этого ключа не задано"
                data[key]= value                
while flag:
    try:
        key = input("Введите ключ>>> ")
        print ("Ключ>>>", key," Значение>>>", data[key])   
    except:
        print("Ключ>>>", key," Значение>>> Такого ключа не существует")
   
    
    q = 0
    i = 2
    while True:
        if q == 3:
            exit()
        command = input("Хотите повторить? Да\Нет>>> ").lower()
        if command == "да":
            break
        elif command == "нет":
            flag = False 
            break
        else: 
            if i == 0:
                print("Все попытки исчерпаны,программа завершается ")
            print("Некоректный ввод. Попыток осталось>>>",i)   
            q+=1 
            i-=1










