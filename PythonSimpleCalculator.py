print("<--- All this code credit goes to **Harkaran Singh** --->")
print("<--- Welcome to our program --->")
print("<--- Please press Ctrl+C to exit the program --->")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
calc = input("Enter the method of calculation: ")

try: 
    while True:
        if calc == '+':
            print(num1 + num2)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            calc = input("Enter the method of calculation: ")

        elif calc == '-':
            print(num1 - num2)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            calc = input("Enter the method of calculation: ")

        elif calc == '*':
            print(num1 * num2)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            calc = input("Enter the method of calculation: ")

        elif calc == '/':
            print(num1 / num2)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            calc = input("Enter the method of calculation: ")

        elif calc == '%':
            print(num1 & num2)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            calc = input("Enter the method of calculation: ")

except KeyboardInterrupt:
    pass