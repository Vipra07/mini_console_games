def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1/ n2

def calculator():
    import art
    print(art.logo)

    operations = {"+": add, "-": sub, "*": mult, "/": div}

    no_1 = float(input("What's the first number?: "))
    cont = True
    while cont:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        no_2 = float(input("What's the next number?: "))
        answer = float(operations[operation](no_1, no_2))
        print(f"{no_1} {operation} {no_2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            no_1 = answer
        else:
            cont = False
            print("\n"*20)
            calculator()

calculator()
