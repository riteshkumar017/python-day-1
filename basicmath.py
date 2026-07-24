print("Basic Math execution")
choice2 =1
while choice2 ==1:
    x=int(input("enter first number:"))
    y=int(input('enter second number:'))
    print("<<<<these are the options>>>>")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    choice = str(input("enter your choice :"))
    a = x+y
    b = x-y
    c = x*y
    d =x/y
    if choice == 1:
            print("addition is",a)
    elif choice ==2:
            print("Subtraction  is",b)
    elif choice ==3:
            print("multiplication Is ",c)
    elif choice ==4:
        print("division is ",d)
    else:
        print(":::you have entered invalid option:::")
    
    print("1.do it again")
    print("2.exit")
    choice2 =int(input("enter what you want :"))

print("THANK YOU ")



