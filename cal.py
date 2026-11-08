def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

print("Select your method:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice(1/2/3/4): ") #taking choice from user
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: ")) #float'll convert a number into a decimal number like 3 into 3.0
            num2 = float(input("Enter the second number:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        else:
            print("Not a good choice. Enter 1,2,3 or 4 please.")
            continue

 #Checking if a user wants another calculation. Break the while loop if answer is no
    next_calculation = input("Another calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Lets gooooooooooooo!!")