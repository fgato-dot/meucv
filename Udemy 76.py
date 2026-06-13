def add(n1, n2):
    return n1 + n2


# TODO: Write out the other3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
# TODO : aDD these 4 functions into a dictionary as the values. Keys="+", "-", "*", "/"

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}




num1 = float(input("What is the first number? :"))


for symbol in operations:
    print(symbol)


operation_symbol = input("Pick an Operation: ")
num2 = float(input("What is the next number?: "))
print(operations[operation_symbol](num1, num2))

