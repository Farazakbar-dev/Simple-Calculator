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
        char = input(f"Please select the character from {characters}: ")
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
    return result



while True: 
    result =  calculate()
    print(f"Result: {result:.2f}")   
    prompt = input("Calculate again (Yes/No): ")
    if prompt.lower() == 'yes': 
        continue
    break 

want_history = input("Enter H for history (or any key to exit): ")
if want_history.lower() == 'h': 
    print("\n",history)
    print("-----------------------------\nThank you for using calculator!")
else: 
    print("-------------------------------\nThank you for using calculator!")
