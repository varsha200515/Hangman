#The Hangman is among the most highly recommended projects to master python for beginners.


word = input("Enter a word(admin)")
print(30*"\n")
newword = list(word)
lenght = len(newword)
dash = list(lenght*"_")
print("The question is",lenght*"_ ")
breakouter = False                                            #with the help of ChatGPT
n = 0
for i in range(1,51):
    letter = input("Enter the letter")
    if letter in newword:
        print("One right guess")
        for k in range(lenght):
            if newword[k] == letter:
                x = dash.pop(k)
                dash.insert(k,letter)
                str1 = " ".join(dash)
                print(str1)

    elif letter not in newword:
        print("Wrong Guess")
        n = n + 1                                              # Initialised n as 0
        if n == 7:
            print("GAME OVER")
            breakouter = True
    if breakouter == True:
        break

    if dash == newword:
        print("You WON !! in ",i,"tries")
        break