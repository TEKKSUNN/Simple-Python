""" To-Do List Manager in Python Written By Emmanuel Leu Tecson """
import os
from time import sleep as wait

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_options(options: list):
    count = 1
    for option in options:
        print(f"{count}. {option}")
        count += 1

def hl_print(strng: str):
    print(f"*** {strng} ***")

def dl_print(strng: str):
    wait(1)
    print(strng)
    wait(3)

def newline():
    print("\n")

make_int_options = lambda options: [i + 1 for i in range(len(options))]
show_int_value_error = lambda: dl_print("Error: Please enter an integer-type value.")
show_not_option = lambda: dl_print("Please choose from the options given.")

class GetIntegerInput:
    def __init__(self, strng: str, options: list):
        self.strng = strng
        self.options = options

    def get_input(self):
        if self.strng == None:
            raise SyntaxError("PLEASE ADD A STRING")
        if self.options == None:
            while True:
                try:
                    answer = int(input(self.strng))
                except ValueError:
                    show_int_value_error()
                    newline()
                    continue
                return answer
        else:
            integer_list = make_int_options(self.options)
            while True:
                try:
                    answer = int(input(self.strng))
                    if answer not in integer_list:
                        show_not_option()
                        newline()
                        continue
                except ValueError:
                    show_int_value_error()
                    newline()
                    continue
                return answer


class TDLManager:
    def __init__(self, todo_list):
        self.tdl = todo_list

    def show_title(self):
        print(r"""
     __     __  _____ ___        ____   ___    _     ___ ____ _____  __     __    
    / /    / / |_   _/ _ \      |  _ \ / _ \  | |   |_ _/ ___|_   _| \ \    \ \   
   / /    / /    | || | | |_____| | | | | | | | |    | |\___ \ | |    \ \    \ \  
  / /    / /     | || |_| |_____| |_| | |_| | | |___ | | ___) || |     \ \    \ \ 
 /_/    /_/      |_| \___/      |____/ \___/  |_____|___|____/ |_|      \_\    \_\
                                                                                   
 __     __      __  __    _    _   _    _    ____ _____ ____             __     __
 \ \    \ \    |  \/  |  / \  | \ | |  / \  / ___| ____|  _ \           / /    / /
  \ \    \ \   | |\/| | / _ \ |  \| | / _ \| |  _|  _| | |_) |         / /    / / 
   \ \    \ \  | |  | |/ ___ \| |\  |/ ___ \ |_| | |___|  _ <         / /    / /  
    \_\    \_\ |_|  |_/_/   \_\_| \_/_/   \_\____|_____|_| \_\       /_/    /_/   
                                                                                  """)
    
    def error_tdl(self, option: int):
        match option:
            case 1:
                dl_print("Error: No To-Do List Detected or To-Do List is empty.")
                
    def go_to_option(self, option: int):
        def create_tdl():
            def show_tdl(tdl):
                count = 1
                newline()
                print("*** TO-DO LIST ***")
                for task in tdl:
                    print(f'{count}. {task}')
                    count += 1
                newline()
                wait(1)

            new_tdl = list()
            newline()
            print("*** CREATING TO-DO LIST ***")
            while True:
                newline()
                task = input("Enter Task (\"ls\" = show list, \"::q\" = quit): ")
                if len(task.split(" ")) == 0:
                    print("Please Enter Something.")
                    wait(3)
                    newline()
                    continue
                if task == '::q':
                    if len(new_tdl) == 0:
                        print("Your To-Do List is Empty.\nAdd Something First You Idiot.")
                        wait(3)
                        newline()
                        continue
                    break
                if task == 'ls':
                    show_tdl(new_tdl)
                    wait(3)
                    continue
                new_tdl.append(task)
                print(f'Successfully added \'{task}\' to the to-do list.')
            newline()
            print("Successfully made to-do list.")
            wait(3)
            newline()
            self.tdl = new_tdl
            self.options()

        def create_question():
            createq_choices = ['Y', 'N']
            while True:
                createq = input("Would you like to create a to-do list?[Y/N]: ").upper()
                if createq not in createq_choices:
                    print("Please Enter \'Y\' or \'N\'.")
                    wait(3)
                    newline()
                    continue
                if createq == 'Y':
                    wait(3)
                    create_tdl()
                else:
                    newline()
                    self.options()
                break


        def show_tdl(tdl):
            if len(tdl) == 0:
                self.error_tdl(1)
                create_question()
            else:
                count = 1
                newline()
                print("*** TO-DO LIST ***")
                for task in tdl:
                    print(f'{count}. {task}')
                    count += 1
                newline()
                wait(3)
        
        def mod_tdl(tdl):
            def add_item_to_list(lst: list):
                while True:
                    newline()
                    item = input("Enter task to add(\"ls\" to show list, \"::q\" to quit): ")
                    if len(item.split(" ")) == 0:
                        print("Please Enter Something.")
                        wait(3)
                        newline()
                        continue
                    if item == '::q':
                        break
                    if item == 'ls':
                        show_tdl(lst)
                        continue
                    if item in lst:
                        print(f'\"{item}\" is already in the to-do list.')
                        wait(3)
                        continue
                    lst.append(item)
                    print(f"Successfully added \'{item}\' to the to-do list.")
                mod_tdl(lst)

            
            def remove_item_from_list(lst: list):
                while True:
                    newline()
                    item = input("Enter task to remove(\"ls\" to show list, \"::q\" to quit): ")
                    if len(item.split(" ")) == 0:
                        print("Please Enter Something.")
                        wait(3)
                        newline()
                        continue
                    if item == '::q':
                        break
                    if item == 'ls':
                        show_tdl(lst)
                        continue
                    if item not in lst:
                        print(f'\"{item}\" is not in the to-do list.')
                        wait(3)
                        continue
                    lst.remove(item)
                    print(f"Successfully removed \'{item}\' from the to-do list.")
                mod_tdl(lst)


            if len(tdl) == 0:
                self.error_tdl(1)
                create_question()
            else:
                while True:
                    if len(tdl) == 0:
                        break
                    newline()
                    print("*** MODIFYING TO-DO LIST ***")
                    options = ["Show To-Do List", "Add Item", "Remove Item", "Exit"]
                    show_options(options)
                    option = GetIntegerInput(strng="Enter your option: ", options=options).get_input()
                    match option:
                        case 1:
                            show_tdl(tdl)
                            continue
                        case 2:
                            add_item_to_list(tdl)
                            continue
                        case 3:
                            remove_item_from_list(tdl)
                            continue
                        case 4:
                            self.options()
                            break
                    print("Please Choose From The Number Before the Options.")
                    wait(3)
                    continue

        match option:
            case 1:
                show_tdl(self.tdl)
                self.options()
            case 2:
                create_tdl()
            case 3:
                self.tdl = mod_tdl(self.tdl)
                self.options()
            case 4:
                print("Goodbye!")
        
    def options(self):
        wait(1)
        newline()
        options = ["Show To-Do List", "Create To-Do List", "Modify To-Do List", "Exit"]
        hl_print("OPTIONS")
        show_options(options)
        option = GetIntegerInput(strng="Enter your option: ", options=options).get_input()
        self.go_to_option(option)
        
    def runConsole(self):
        clear()
        self.show_title()
        input("Press Enter to Continue...")
        print("\n")
        self.options()


if __name__ == '__main__':
    tdl = list()
    program = TDLManager(tdl)
    program.runConsole()
