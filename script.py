print("\n************************* Python Calculator***********************************\n")
first_number = 0.0
second_number = 0.0
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
    return num1 / num2

# exponentiate function
def exp(num1, num2): 
    return num1 ** num2


while True: 
    try: 
        first_number = float(input("enter first number (1 - 100): "))
        if first_number > 100: 
            raise ValueError
         
    except ValueError as err: 
        print(err, "Invalid Input!")
    else: 
        print(f"You entered {first_number} as first number.")
        break


    
while True: 
    try: 
        second_number = float(input("enter second number (NOT 0, 1 - 100): "))
        if second_number > 100: 
            raise ValueError
        if second_number == 0: 
            raise ZeroDivisionError
    except ValueError as err: 
        print(err, "Invalid Input!")
    except ZeroDivisionError as err: 
        print(err, "You can't divide by zero")
    else: 
        print(f"You entered {second_number} as second number.")
        break 
char = ''
result = 0.0
while True: 
    char = input(f"Please select the character from {characters}: ")
    if char in characters: 
        
        if char == '+': 
            result = add(first_number, second_number)

        elif char == '-': 
            result = subtract(first_number, second_number)

        elif (char == '*'): 
            result = multiply(first_number, second_number)

        elif char == '/': 
            result = divide(first_number, second_number)

        elif char == '**': 
            if second_number < 0: 
                print("Can't be raised to a negative power.")
            else:
                result = exp(first_number, second_number) 
        break
    else:        
        print(f"{char} is not in {characters}")

      
print("--------------------------")
print(f"Your first number is {first_number}\nAnd your second number is {second_number}")
print(f"You selected {char} from {characters}")

print(f"Result: {result}")





