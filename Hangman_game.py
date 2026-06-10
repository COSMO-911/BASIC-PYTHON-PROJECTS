import random


words =[
    "people", "thing", "woman", "child", "world", 
    "school", "family", "student", "group", "country", 
    "problem", "place", "company", "system", "program", 
    "question", "government", "number", "night", "mother", 
    "money", "story", "month", "business", "issue", 
    "computer", "animal", "music", "movie", "nature", 
    "science", "history", "river", "ocean", "planet", 
    "forest", "desert", "mountain", "society", "reason", 
    "person", "minute", "office", "father", "health", 
    "result", "power", "market", "water", "member"
]


#Ascii Art

hangman = { 0 :("   ",
                "   ",
                "   "),
            1: (" O ",
                "   ",
                "   "),
            2: (" O ",
                " | ",
                "   "),
            3: (" O ",
                "/| ",
                "   "),
            4: (" O ",
                "/|\\ ",
                "   "),
            5: (" O ",
                "/|\\  ",
                "/  "),
            6: (" O ",
                "/|\ ",
                "/ \\ "),}

def display_man(wrong_guesses ):
    print("###############")
    for line in hangman[wrong_guesses]:
        print(line)
    print("###############")

    
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"correct answer is :{' '.join(answer)}")


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses )
        display_hint(hint)
        guess = input("guess a letter: ").lower()
    
        if len(guess) != 1 or not guess.isalnum() :
            print("invalid guess, one letter at a time")
            continue
        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            print("incorrect guess")
            wrong_guesses +=1 
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("you win")
            is_running = False
        elif wrong_guesses>= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("fahhh!!  out of guesses")
            print("you lose")
            is_running = False

if __name__ == "__main__":
    main()

    
