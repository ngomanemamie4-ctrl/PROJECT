num1 = int(input("enter the number:"))
num2 = int(input("enter the number"))
print ("*menu*/n1. +/2.-/n3.*/n4.%")
ch= int(input("enter the choice:"))
if ch ==1:
    print ("result:",num1+num2)
elif ch==2:
    print ("result:",num1-num2)
elif ch==3:
    print ("result:",num1*num2)
elif ch==4:
    print ("result:",num1%num2)