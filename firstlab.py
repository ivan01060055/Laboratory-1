print("Welcome to the common calculator programm")

flag = True
while (flag == True):
    val1 = int(input("input the first value ="))
    val2 = int(input("input the second value = "))

    command = input("input your operation (+,-,*,/):")

    #command = [+,-,*,/]
    if command == '+':
        print(val1 + val2)
    elif command =='-':
        print(val1 - val2)   
    elif command =='*':
        print(val1 * val2)   
    elif command =='/':
        print(val1 // val2)  
    else:
        print("wrong operation")             
    for i in range(3):
        command = input("Do you want to continue? (Y/N):")
        if command == 'Y' or command == 'y':
            break
        elif command == 'N' or command == 'n':
            flag = False
            break
        else:
            print("Wrong command")
            i += 1
        if i == 3:
            print ("too much errors ")
            flag = False
            break
           
                
           
            










