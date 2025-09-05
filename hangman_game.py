import random
from hangman_words import words


#dictionary of key:()

hangman_art={0: ("   ",
                  "   ",
                  "   ",), 
              1: (" o ",
                  "   ",
                  "   ",),
              2: (" o ",
                  " | ",
                  "   ",),
              3: (" o ",
                  "/| ",
                  "  ",),
              4: (" o ",
                  "/|\\ ",
                  "  ",),
              5: (" o ",
                  "/|\\ ",
                  "/ ",),
              6: (" o ",
                  "/|\\ ",
                  "/ \\ ",),}




def display_man(wrong_guesses):
    print("********************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("********************************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))
    


def main():
    answer=random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("enter a letter:  ").lower()
        
        
        #enter single character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue    
        
        guessed_letters.add(guess)

        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")
            if wrong_guesses == 6:
                print("You lost! The answer was:", answer)
                is_running = False
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word:", answer)
            is_running = False    

if __name__ == "__main__":
    main()
    
                    

