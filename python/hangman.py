def play():
    print("*******************")
    print("Hangman Game")
    print("*******************")

    secret_word       = "banana".upper()
    hit               = False
    hanged            = False
    hitted_characters = ["_" for char in secret_word]
    mistakes          = 0

    while(not hanged and not hit):
        print("The word is {}".format(hitted_characters))
        response = input("Type a letter of the secret word:").strip().upper()

        if(response in secret_word):
            index = 0
            for character in secret_word:
                if(response == character):
                    hitted_characters[index] = response
                index += 1    
        else:
            mistakes+=1

        hanged = mistakes == 6
        hit    = "_" not in hitted_characters
        
    if(hit):
        print("You won. The secret word was {}".format(secret_word))
    elif(hanged):
        print("You loose. The secret word was {}".format(secret_word))

if(__name__ == "__main__"):
    play()