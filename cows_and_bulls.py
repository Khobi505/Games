import random
import string

def cb_game():
    print("Welcome to the Cows and Bulls Game")
    print("-----------------------------------\n\n")
    
    usernum = input("Enter a four digit number:")
    
    alphabets = string.ascii_letters

    print("\n")
    num1 = string.digits
    
    
    list_of_num = []
    list_of_num.extend(list(num1))
    random.shuffle(list_of_num)
    


    secretnum = str(("".join(list_of_num[0:4])))
    
    if len(usernum) != 4:
        print("Please Enter A Four Digit Number!!!!!!!!!!!!!!")
        quit()
    else:
        if usernum[0] == secretnum[0]:
            print("1 Cow, 3 bulls")
            if usernum[1] == secretnum[1]:
                print("1 Cow, 3 bulls")
                if usernum[2] == secretnum[2]:
                    print("1 Cow, 3 bulls")
                    if usernum[3] == secretnum[3]:
                        print("1 Cow, 3 bulls")
                        if usernum[0 : 2] == secretnum[0 : 2]:
                            print("2 Cows, 2 bulls")
                            if usernum[1 : 3] == secretnum[1 : 3]:
                                print("2 Cows, 2 bulls")
                                if usernum[2 : 4] == secretnum[2 : 4]:
                                    print("2 Cows, 2 bulls")
                                    if usernum[0 : 3] == secretnum[0 : 3]:
                                        print("3 Cows, 1 bull")
                                        if usernum[1 : 4] == secretnum[1 : 4]:
                                            print("3 Cows, 1 bull ")
                                            if usernum[0 : 4 ] == secretnum[0 : 4]:
                                                print("4 Cows, 0 bulls")
        else:
            print("NO MATCH!!!!!", "\n0 Cows, 4 bulls")
            print("Please Try Again")
        
    print("\n\n")
    print("The secret number was : ", secretnum)


cb_game()

