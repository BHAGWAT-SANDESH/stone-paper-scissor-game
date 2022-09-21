import random
# "Stone","Paper","Scissor"
while(True):
    options = [1,2,3]
    pc = random.choice(options)

    print("Select one option from below : ")
    print("1 --> Stone \n2 --> Paper \n3 --> Scissor \n9 --> EXIT")

    user_input = int(input("Enter your choice : "))

    if(user_input == 9):
        break
    else:
        print("\nUser selected : ",user_input)
        print("Computer selected : ",pc)
        print()
        print("==========================")
    # 1
        if(user_input == 1 and pc == 1):
            print(f"Match Draw")
        elif (user_input == 1 and pc == 2):
            print(f"Computer Wins")
        elif(user_input == 1 and pc == 3):
            print(f"Player Wins")
    # 2
        elif(user_input == 2 and pc == 1):
            print(f"Player Wins")
        elif(user_input == 2 and pc == 2):
            print(f"Match Draw")
        elif (user_input == 2 and pc == 3):
            print(f"Computer Wins")
    # 3
        elif(user_input == 3 and pc == 1):
            print(f"Computer Wins")
        elif(user_input == 3 and pc == 2):
            print(f"Player Wins")
        elif (user_input == 3 and pc == 3):
            print(f"Match Draw")
    # Default
        else:
            print("invalid Input,Try again")
        print("==========================")
        print()