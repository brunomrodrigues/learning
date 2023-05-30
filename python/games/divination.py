import random

def play():
    print("*******************")
    print("Divination Game")
    print("*******************")

    secret_number                   = random.randrange(1,101)
    round                           = 1
    difficult_level_str             = input("Choose your difficult level: 1 for Easy, 2 for Normal and 3 for Hard:")
    difficult_level                 = int(difficult_level_str)
    user_score                      = 1000

    if(difficult_level == 1):
        total_rounds = 100
    elif(difficult_level == 2):
        total_rounds = 50
    else:
        total_rounds = 25    

    print(secret_number)

    for round in range(total_rounds):
        
        print("Round number {} of {}".format(round + 1, total_rounds))
        response_str                     = input("Type your secret number between 1 and 100:")
        response                         = int(response_str)
        response_in_correct_range        = response > 1 and response < 100
        number_highest_then_response     = response > secret_number
        number_lowest_then_response      = response < secret_number
        hit                              = secret_number == response

        if(response_in_correct_range == 0):
            print("You should type a number between 1 and 100!")
            continue

        if(hit):
            print("You have discovered the secret number and your socre was {}!".format(user_score))
            break
        else:
            if(number_highest_then_response):
                print("Your number is highest than the secret number!")
            elif(number_lowest_then_response):
                print("Your number is lowest than the secret number!")
        
        user_score = user_score - abs(secret_number - response) 

    print("End Game!")

if(__name__ == "__main__"):
    play()