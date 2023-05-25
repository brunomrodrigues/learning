print("*******************")
print("Divination Game")
print("*******************")

secret_number                   = 42
round                           = 1
total_desired_rounds_str        = input("Type how many tries you want:")
total_desired_rounds            = int(total_desired_rounds_str)

while(round <= total_desired_rounds):
    
    print("Round number {} of {}".format(round, total_desired_rounds))
    response_str                     = input("Type your secret number:")
    response                         = int(response_str)
    number_highest_then_response     = response > secret_number
    number_lowest_then_response      = response < secret_number
    hit                              = secret_number == response

    if(hit):
        print("You have discovered the secret number!")
    else:
        if(number_highest_then_response):
            print("Your number is highest than the secret number!")
        elif(number_lowest_then_response):
            print("Your number is lowest than the secret number!")

    round = round + 1

print("End Game!")
