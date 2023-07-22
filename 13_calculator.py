#Calculator
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operation={
        '+':add,
        '-':sub,
        '*':mul,
        '/':div
        }
def calculator():

    still=True
    n1=float(input("Enter the first number : "))
    while still:
        for i in operation:
            print(i)
        task=input("Pick an operation from the above  : ")
        n2=float(input("Enter the second nuber : "))
        operate=operation[task]
        answer=operate(n1,n2)
        print(f"{n1} {task} {n2} = {answer}")
        ask=input(f"Wanna continue with {answer} ? \nyes \nno ")
        if ask == 'yes':
            n1=answer
        else:
            still=False
            calculator()
calculator()