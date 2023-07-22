def prime(num):
    flag = 0
    if num == 1:
        return "Nit a Prime Number"
    for i in range(2, num):
        if num % i == 0:
            flag = 1
    if flag == 1:
        return "It is not a prime number"
    else:
        return "It is a prime number"

number = int(input("Enter the Number : "))
print(prime(13))