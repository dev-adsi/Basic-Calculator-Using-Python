#Calculator Made By Adiya Singh

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
sol=input("Enter the operation you want to do (+,-,*,/)")

if sol=="+":
    a=n1+n2
    print(a)

elif sol=="-":
    a=n1-n2
    print(a)

elif sol=="*":
    a=n1*n2
    print(a)

elif sol=="-":
    a=n1-n2
    print(a)
elif sol=="/":
    a=n1/n2
    print(a)

else:
    print("You have entered the wrong operation")