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

first_number = get_number()
second_number = get_number()
  
char = ''
result = 0.0
while True: 
    char = input(f"Please select the character from {characters}: ")
    if char in characters: 
        
        if char == '+': 
            result = add(first_number, second_number)

        elif char == '-': 
            result = subtract(first_number, second_number)

        elif char == '*': 
            result = multiply(first_number, second_number)

        elif char == '/': 
            try: 
                result = divide(first_number, second_number)
            except ZeroDivisionError as err: 
                print(err, "You can't divide by zero")
                continue
        elif char == '**': 
            result = exp(first_number, second_number) 
        break
    else:        
        print(f"{char} is not in {characters}")

      
print("--------------------------")
print(f"Your first number is {first_number}\nAnd your second number is {second_number}")
print(f"You selected {char} from {characters}")

print(f"Result: {result:.2f}")
