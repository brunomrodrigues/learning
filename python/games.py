import divination
import hangman


print("*******************")
print("*Choose your game!*")
print("*******************")

game_selected = int(input("Choose 1 for Divination Game or 2 for Hangman Game:"))

if(game_selected == 1):
    print("Youre playng Divination!")
    divination.play()
elif(game_selected == 2):
    print("Youre playing Hangman Game!")
    hangman.play()
else:
    print("You dont choose a valid option!")