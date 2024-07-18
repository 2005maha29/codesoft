print("lets start caluclating")
list1=['Add','Sub','Mul','Div']
print(list1)
Operation=input("enter the operation to be performed from list1:")
def cal():
    Number1=int(input("enter the number:"))
    Number2=int(input("enter the number:"))
    if Operation=='Add':
        sum=Number1+Number1
        print("addition of two numbers is:",sum)
    elif Operation=='Sub':
        Difference=Number1-Number2
        print("difference between two numbers is:",Difference)
    elif Operation=='Mul':
        Multiplication=Number1*Number2
        print("Multiplication of two numbers is:",Multiplication)
    elif Operation=='Div':
        list2=['modulo','Division']
        print(list2)
        division=input("select the division operation from the list2:")
        if division=='modulo':
            remainder=Number1%Number2
            print("the remainder is :",remainder)
        elif division=='Division':
            quoient=Number1/Number2
            print("Quoient of two numbers is:",quoient)
        else:
            print("No Division Operation is selcted")
    else:
        print("No NUmbers and Operation was given")
cal()