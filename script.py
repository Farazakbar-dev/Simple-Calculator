print("\n************************* Python Calculator***********************************\n")


characters = ['+', '-', '*', '/', '**']

# Add function
def add(num1, num2): 
    return num1 + num2

# Subtract function
def subtract(num1, num2): 
    return num1 - num2

# Multiply function
def multiply(num1, num2): 
    return num1 * num2

# Divide function
def divide(num1, num2): 
    if num2 == 0: 
        raise ZeroDivisionError
    return num1 / num2

# exponentiate function
def exp(num1, num2): 
    return num1 ** num2

# Here goes the option list [calculation or history]
options_list = ["calculate", "history", "exit"]
def menu(): 
    while True: 
        option = input(f"Select one option from {options_list}").strip().lower()
        if option in options_list: 
            if option == "calculate": 
                calculate()
            elif option == "history": 
                if history: 
                    for num, entry in enumerate(history, 1): 
                        print (f"{num}: {entry}")
                else: 
                    print("No history!")
            elif option == "exit": 
                print("-----------------------------\nThank you for using calculator!")
                break
            
        else: 
            print(f"Please select an option from {options_list}")
                
    
# function get number
def get_number(): 
    while True: 
        try: 
            number = float(input("Enter number: "))
            if number < 0: 
                raise ValueError
        except ValueError: 
            print("Invalid Input! Enter a positive number")
        else: 
            print(f"You entered {number} as input")
            break
    return number


def get_operator():
    while True: 
        char = input(f"Please select the character from {characters}: ").strip()
        if char in characters: 
            return char
        else:        
                print(f"{char} is not in {characters}")
    
history = [] 
def calculate():
    
    char = get_operator() 
    num1 = get_number()
    num2 = get_number()
    
    if char == '+': 
        result = add(num1,num2)

    elif char == '-': 
        result = subtract(num1,num2)

    elif char == '*': 
        result = multiply(num1,num2)

    elif char == '/': 
        while num2 <= 0 : 
            print("You can't divide by zero. Enter a valid number: ")
            num2 = get_number()
        result = divide(num1,num2)  
    elif char == '**': 
        result = exp(num1,num2) 
    string = f"{num1} {char} {num2} = {result}"
    history.append(string)
    print(f"Result: {round(result, 2)}")

menu()

 

# New Objectives: 
    # 1. List some options such as Calculate, History etc.. // Done
    # 2. Users should be able to view the history without even jumping to calculations // Done
    # 3. Users should be able to edit the history (delete)
    