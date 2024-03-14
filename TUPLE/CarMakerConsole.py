""" Car Maker Console Application in Python """
# Using tuples
def make_car(collection):
    def make_set(strng: str):
        foo = set()
        for i in strng:
            foo.add(i)
        return foo

    print('\n*** MAKING CAR ***')
    while True:
        name = input('Enter car\'s name: ')
        color = input('Enter car color\'s name: ')
        brand = input('Enter car brand\'s name: ')
        while True:
            try:
                car_number =int(input('Enter car\'s stock number: '))
            except ValueError:
                print("Error: please enter a number.\n")
                continue
            break
        if len(name) == 0 or len(color) == 0 or len(brand) == 0:
            print("Error: please enter something on all properties.\n")
            continue
        if len(make_set(name)) == 1 or len(make_set(color)) == 1 or len(make_set(brand)) == 1:
            print("Error: please put more than one character on all properties.\n")
            continue
        car = (name, color, brand, car_number)
        if car in collection:
            print("You already have this car in your collection.\n")
            continue
        print("\n*** CAR SUCCESSFULLY MADE ***\n")
        collection.append(car)
        return None

def show_collection(collection):
    if len(collection) == 0:
        print("You haven't made a single car.\n")
    else:
        print('\n*** COLLECTION ***')
        count = 0
        for car in collection:
            count += 1
            print(f'{count}.\tName: {car[0]}\tColor: {car[1]}\tBrand: {car[2]}\tStock Number : {car[3]}')

def option_get(choices):
    print('\n*** OPTIONS ***')
    count = 0
    int_choices = []
    for choice in choices:
        print(f'{count + 1}. {choice}')
        count += 1
        int_choices.append(count)
    while True:
        try:
            option = int(input('Go to : '))
            if option not in int_choices:
                print("Error: please choose from the numbers given before the options.\n")
                continue
        except ValueError:
            print("Error: please give an integer-type value.\n")
            continue
        return option

def go_to(option):
    global car_collection
    match option:
        case 1:
            show_collection(car_collection)
        case 2:
            make_car(car_collection)
        case 3:
            print("\nGoodbye!")
            return 1

if __name__ == '__main__':
    print("Welcome to Car Maker!")
    input("\nPress Enter to continue...")
    car_collection = []
    while True:
        options = ["Show Collection", "Make Car", "Exit Program"]
        option = option_get(options)
        stopq = go_to(option)
        if stopq == 1:
            break
        continue
