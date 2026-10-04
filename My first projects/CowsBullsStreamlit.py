import streamlit as st

secret = "1896"
word_given = st.text_input("Guess a number! ")
guess = str(word_given)

Bulls = 0
Cows = 0

if len(guess) == 4:
    for i in range(4):
        if guess[i] in secret:
            if guess [i] == secret [i]:
                Bulls = Bulls + 1
            else:
                Cows = Cows + 1
        else: 
            Bulls = Bulls + 0
            Cows = Cows + 0

    st.write("Bulls: " + str(Bulls) + ", Cows:" + str(Cows))

