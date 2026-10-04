Solution = "lösung"

Mistakes = 0
Correct = 0
Mistakes_left = 6 - Mistakes
visible = ""

while Mistakes < 6:

    guess = input("Guess a lower-case letter!")

    if guess in Solution:
        Correct += 1
    else:
        Mistakes += 1

    for i in guess:
        if i in Solution:
            visible = str(visible) + str(guess)
        else:
            visible = str(visible)

    print("Your Guess: " + str(guess))
    print("Correct: " + str(Correct))
    print("Mistakes: " + str(Mistakes))
    print("Mistakes left: " + str(Mistakes_left))
    print("So far you have: " + str(visible)) #hier noch richtig ordnen!!

    if set(visible) == set(Solution):
        Word_Guess = input("You guessed the right letters, congrats! Now try to guess the word from your letters:") ##

        if Word_Guess == Solution:
            print("Great Success!")
        else:
            print("Try again! The solution would have been 'lösung'")
        break


if Mistakes == 6:
    print("Better luck next time! The correct word was 'lösung'.")