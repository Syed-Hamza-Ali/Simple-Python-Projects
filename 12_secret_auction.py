#Secret Auction

buyer={}
still=1
highest=0
winner=""

while still==1:

    key=input("Enter your Name : ")
    value=int(input("Enter the Price : "))
    buyer[key]=value
    check=input("Are there any other buyers?\n1)Yes\n2)No")

    if check=='2':
        still=0

for i in buyer:

    bid=buyer[i]
    if bid>highest:
        highest=bid
        winner=i

print(f"{winner} has the highest auction of {highest}")