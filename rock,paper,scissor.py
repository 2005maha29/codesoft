import random
def computer_choice():
    return random.choice(lis)
lis=['rock','paper','scissors']
user_choice=input("Enter the user choice(rock,paper,scissor)").lower()
if user_choice not in lis:
    print("invalid choice,Enter the correct from the above mentioned:")
else:
    com_choice=computer_choice()
    print("computer choice choice is:",com_choice)
    if user_choice==com_choice:
        print("It's a Tie")
    elif user_choice=='rock' and com_choice=='scissors':
        print("You Have won the match ")
    elif user_choice=='paper' and com_choice=='rock':
        print("You Have won the match")
    elif user_choice=='scissors' and com_choice=='paper':
        print("You Have won the match")
    else:
        print("computer won the match")