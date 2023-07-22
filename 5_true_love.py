# True Love

name1 = input("Enter your Name : ")
name2 = input("Enter their Name : ")
name1 = name1.lower()
name2 = name2.lower()
t = 0
l = 0
t += (name1+name2).count('t')
t += (name1+name2).count('r')
t += (name1+name2).count('u')
t += (name1+name2).count('e')
l += (name1+name2).count('l')
l += (name1+name2).count('o')
l += (name1+name2).count('v')
l += (name1+name2).count('e')
print("You score is ", l+t)