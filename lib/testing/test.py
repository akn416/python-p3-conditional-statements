# def calculator(operation, num1, num2):
#     if operation == "+":
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         return num1 / num2
#     else:
#         print ("Invalid Operation")
#         pass

# calculator('a', 1, 2)

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!") 
        return None
    
print(calculator("a", 1, 2))
