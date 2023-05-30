import random

def play():
    
    hit               = False
    hanged            = False
    mistakes          = 0

    print_welcome_message()
    secret_word = choose_secret_word()
    hitted_characters = start_hitted_chars(secret_word)
   
    while(not hanged and not hit):
        print("The word is {}".format(hitted_characters))
        response = ask_response()

        if(response in secret_word):
            mark_correct_char(response, secret_word, hitted_characters)
        else:
            mistakes+=1    
           

        hanged = mistakes == 6
        hit    = "_" not in hitted_characters
        
    if(hit):
        print_winner_message()
    elif(hanged):
        print_loser_message(secret_word)

def print_welcome_message():
    print("*******************")
    print("Hangman Game")
    print("*******************")

def choose_secret_word():
    word_file         = open("words.txt", "r", encoding='utf-8')
    
    words = []
    for line in word_file:
        line = line.strip()
        words.append(line.upper())

    drawn_number = random.randrange(0, len(words))
    secret_word = words[drawn_number]
    return secret_word

def start_hitted_chars(word):
    return ["_" for char in word]

def ask_response():
    return input("Type a letter of the secret word:").strip().upper()

def mark_correct_char(response, secret_word, hitted_characters):
    index = 0
    for character in secret_word:
        if(response == character):
            hitted_characters[index] = response
        index += 1    

def print_winner_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("Ops! You´re hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    play()