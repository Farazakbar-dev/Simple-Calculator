print("\n************************* Python Calculator***********************************\n")
characters = ['+', '-', '*', '/', '**']
history = [] 
options_list = ["calculate", "history", "exit"]
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


# Main function
def main(): 
    while True: 
        option = input(f"Select one option from {options_list}").strip().lower()

        if option == "calculate" or option == 'c': 
            calculate()
        elif option == "history" or option == 'h': 
            show_history()
        elif option == "exit" or option == 'e': 
            print("-----------------------------\nThank you for using calculator!")
            break           
        else: 
            print(f"Please select an option from {options_list}")
                
    
# function to get number from user
def get_number(): 
    while True: 
        try: 
            number = float(input("Enter number: "))
        except ValueError: 
            print("Invalid Input! Enter a positive number")
        else: 
            print(f"You entered {number} as input")
            break
    return number

#operator function takes operator as input from user
def get_operator():
    while True: 
        char = input(f"Please select the character from {characters}: ").strip()
        if char in characters: 
            return char
        else:        
                print(f"{char} is not in {characters}")
    

# history functions prints history
def show_history(): 
    if history: 
        for num, entry in enumerate(history, 1): 
            print (f"{num}: {entry}")
    else: 
        print("No history!")
        
# Calculate function
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
        while num2 == 0 : 
            print("You can't divide by zero. Enter a valid number: ")
            num2 = get_number()
        result = divide(num1,num2)  
    elif char == '**': 
        result = exp(num1,num2) 
    string = f"{num1} {char} {num2} = {round(result,2)}"
    history.append(string)
    print(f"Result: {round(result, 2)}")


main()

    