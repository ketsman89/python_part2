import os

menu = {1:"Вывести список пользлвателей", 2:"создать пользователя"}
list_users = {3: "Валера", 4: "Боря"}

def create_user():
    pass

def list_users():
    print(list_users)

def clear_screen():
    os.system("cls")
    

def print_menu_and_get_option():
    print(menu)
    option = input("enter your choice: ")
    clear_screen()
    return option

def process_option(option):
    if option == 1:
        list_users()
    elif option == 2:
        create_user()
    elif option == 3:
        pass
    elif option == 4:
        pass

def main():
    
    while True:
        option = print_menu_and_get_option()        
        process_option(option)

if __name__ == "__main__":        
    main()