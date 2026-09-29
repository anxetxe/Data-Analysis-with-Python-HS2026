secret = "1896"
word_given = input("Guess a number! ")
guess = str(word_given)

Bulls = 0
Cows = 0

for i in range(4):
    if guess[i] in secret:
        if guess [i] == secret [i]:
            Bulls = Bulls + 1
        else:
            Cows = Cows + 1
    else: 
        Bulls = Bulls + 0
        Cows = Cows + 0

print("Bulls: " + str(Bulls) + ", Cows:" + str(Cows))
