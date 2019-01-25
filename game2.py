'''
Evan Watson, Ryan Pike
1-18-19
v2.4.10
Wheel O' Good Luck
'''
import random

#defining vars
    
vowel = ['a', 'e', 'i', 'o', 'u', 'y']

consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

#opening the word list (the words to guess)

file = open("wordlist.txt", "r")

text = file.read()

file.close()

#turning that file into a list

wordlist = text.split()

#setting the guessing word by randomly chosing a string in the list

word = random.choice(wordlist)
blank = []
for letter in word:
    blank.append('_')
    
#acts as a 'spinner'

wheel = random.randint(1,5)

#defining main function
def main(money, wheel, consonant_letter, vowel_letter):
    money = 0
    if wheel == 1:
        choice1 = input("Congratulttions, you won $1000! there are " + str(len(word)) + " letters in this word. Would you like to buy a (c)onsonant or a (v)owel? ").lower()
        money += 1000
        if choice1 == 'vowel' or choice1 == 'v':
            vowel_f(money, word, vowel, consonant_letter, vowel_letter)
        elif choice1 == 'consonant' or choice1 == 'c':
            consonant_f(money, word, consonant, vowel_letter)
        else:
            print("Please enter 'c', or 'v'")
            wheel = 1
            main(money, wheel, consonant_letter, vowel_letter)
            
    elif wheel == 2:
        choice2 = input("Congratulations, you won $5000! there are " + str(len(word)) + " letters in this word. Would you like to buy a consonant or a vowel? ").lower()
        money += 5000
        if choice2 == 'vowel' or choice2 == 'v':
            vowel_f(money, word, vowel, consonant_letter, vowel_letter)
        elif choice2 == 'consonant' or choice2 == 'c':
            consonant_f(money, word, consonant, vowel_letter)
        else:
            print("Please enter 'c', or 'v'")
            wheel = 2
            main(money, wheel, consonant_letter, vowel_letter)
            
    elif wheel == 3:
        choice3 = input("Congratulations, you won $10000! there are " + str(len(word)) + " letters in this word. Would you like to buy a consonant or a vowel? ").lower()
        money += 10000
        if choice3 == 'vowel' or choice3 == 'v':
            vowel_f(money, word, vowel, consonant_letter, vowel_letter)
        elif choice3 == 'consonant' or choice3 == 'c':
            consonant_f(money, word, consonant, vowel_letter)
        else:
            print("Please enter 'c', or 'v'")
            wheel = 3
            main(money, wheel, consonant_letter, vowel_letter)
            
    elif wheel == 4:
        choice4 = input("Congratulations, you won the jackpot($100000)! there are " + str(len(word)) + " letters in this word. Would you like to buy a consonant or a vowel? ").lower()
        money += 100000
        if choice4 == 'vowel' or choice4 == 'v':
            vowel_f(money, word, vowel, consonant_letter, vowel_letter)
        elif choice4 == 'consonant' or choice4 == 'c':
            consonant_f(money, word, consonant, vowel_letter)
        else:
            print("Please enter 'c', or 'v'")
            wheel = 4
            main(money, wheel, consonant_letter, vowel_letter)
            
    elif wheel == 5:
        print("Sorry, you went bankrupt. Please try again")
        money += 0
        main(money, wheel, consonant_letter, vowel_letter)
        
#defining the vowel function
        
def vowel_f(money, word, vowel, consonant_letter, vowel_letter):           
    vowel_letter = input("Vowels cost $500 each, what vowel would you like to buy? ").lower()
    if vowel_letter in vowel:
        print("You have chosen " + vowel_letter + ".")
        money -= 500
        if vowel_letter in word:
            print("There are " + str(word.count(vowel_letter)) + " " + vowel_letter + "'s in this word")
            wordblanks(vowel_letter, consonant_letter, money)
            if '_' not in blank:
                finish(money)
            elif '_' in blank:
                choose_again(vowel_letter, consonant_letter, money) 
        else:
            print("Sorry, the letter you guessed is not in this word")
            choose_again(vowel_letter, consonant_letter, money)
    else:
        print("That is not a vowel, please enter a vowel.")
        vowel_f(money, word, vowel, consonant_letter, vowel_letter)
        
#making the blanks in the word & replacing them with letters as they are guessed
        
def wordblanks(vowel_letter, consonant_letter, money):
    for letter in range(len(blank)):
        if word[letter] == vowel_letter:
            blank[letter] = vowel_letter
        elif word[letter] == consonant_letter:
            blank[letter] = consonant_letter
    print(' '.join(blank))
    
#defining the consonant function
    
def consonant_f(money, word, consonant, vowel_letter):           
    consonant_letter = input("What consonant would you like to guess? ").lower()
    if consonant_letter in consonant:
        print("You have chosen " + consonant_letter + ".")
        if consonant_letter in word:
            print("There are " + str(word.count(consonant_letter)) + " " + consonant_letter + "'s in this word")
            wordblanks(vowel_letter, consonant_letter, money)
            if '_' not in blank:
                finish(money)
            elif '_' in blank:
                choose_again(vowel_letter, consonant_letter, money)  
        else:
            print("Sorry, the letter you guessed is not in this word")
            choose_again(vowel_letter, consonant_letter, money)
    else:
        print("That is not a consonant, please enter a consonant.")
        consonant_f(money, word, consonant, vowel_letter)
                
#defining the choose again, asks user whether they want to buy a vowel or consonant
        
def choose_again(vowel_letter, consonant_letter, money):
    spin_again = input("Would you like to buy another (v)owel or (c)onsonant? ").lower()
    if spin_again == 'c' or spin_again == 'consonant':
        consonant_f(money, word, consonant, vowel_letter)
    elif spin_again == 'v' or spin_again == 'vowel':
        vowel_f(money, word, vowel, consonant_letter, vowel_letter)
    elif spin_again == 'n' or spin_again == 'no':
        print("Very well...")
    else:
        print("Please enter 'c', 'v', or 'no'")
        choose_again(vowel_letter, consonant_letter, money)
        
#defining the final function, when the game is over
        
def finish(money):
    print("You have won!! Congrats on winning Wheel O' Good Luck")
    play_again = input("Would you like to play again? ")
    if play_again == 'y' or play_again == 'yes':
        main(money, wheel, consonant_letter, vowel_letter)
    elif play_again == 'n' or play_again == 'no':
        print("Have a good day!")
        print("Game Over. You finished with $" + str(money))
#calling the actual start of the program, which in this case is main()
money = 0
consonant_letter = True
vowel_letter = True
while consonant_letter == True:
  message = '''
  Welcome to Wheel O' Good Luck!!
  Rules:
  1. You must specify what type of letter you want.
  2. You can either use the first letter of each word or you can type the whole word (i.e. consonant can be 'c' or 'consonant')
  3. Don't cheat!
  '''
  print(message)
  break
main(money, wheel, consonant_letter, vowel_letter)
