#
def get_factorial(num):
    factorial = 1
    
    for n in range(1, num + 1):
        factorial *= n

    return factorial

def sum_odd_numbers(num):
    sum = 0
    indx = 0

    while(indx <= num):
        if(indx % 2 == 1):
            sum += indx

        indx += 1
    
    return sum

def display_menu():
    print('1-Factorial')
    print('2-Sum odd numbers')
    print('3-Exit')

def run_menu():
    menu_option = "0"

    while(menu_option != "3"):
        display_menu()
        menu_option = input("Enter option: ")
        handle_menu_option(menu_option)

        if(menu_option == "3"):
            exit_option = input("Are you sure you want to exit type Y: ")
            
            if(not(exit_option == "y" or exit_option == "Y")):
                menu_option = "0"

def handle_menu_option(menu_option):
    if(menu_option != "3"):
        num = int(input("Enter num: "))

    if(menu_option == "1"):
        factorial = get_factorial(num)
        print("Factorial: ", factorial)
    elif(menu_option == "2"):
        sum = sum_odd_numbers(num)
        print("Odd sum: ", sum)
    elif(menu_option == "3"):
        print("You typed exit...")
    else:
        print("Invalid option")




    
