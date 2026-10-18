import streamlit as st

Solution = "lösung"

if "Mistakes" not in st.session_state:
    st.session_state.Mistakes = 0
    st.session_state.Correct = 0
    st.session_state.visible = ""
    st.session_state.stage = "letters"

if st.session_state.stage == "letters" and st.session_state.Mistakes < 6:

    with st.form("letter_form", clear_on_submit=True):
        guess = st.text_input("Guess a lower-case letter!")
        submitted = st.form_submit_button("Guess")

    if submitted:

        if guess in Solution:
            st.session_state.Correct += 1
        else:
            st.session_state.Mistakes += 1

        for i in guess:
            if i in Solution:
                st.session_state.visible = str(st.session_state.visible) + str(guess)
            else:
                st.session_state.visible = str(st.session_state.visible)

        Mistakes_left = 6 - st.session_state.Mistakes

        st.write("Your Guess: " + str(guess))
        st.write("Correct: " + str(st.session_state.Correct))
        st.write("Mistakes: " + str(st.session_state.Mistakes))
        st.write("Mistakes left: " + str(Mistakes_left))
        st.write("So far you have: " + str(st.session_state.visible)) #hier noch richtig ordnen!!

        if set(st.session_state.visible) == set(Solution):
            st.session_state.stage = "word"

if st.session_state.stage == "word":
    with st.form("word_form"):
        Word_Guess = st.text_input("You guessed the right letters, congrats! Now try to guess the word from your letters:") ##
        word_submitted = st.form_submit_button("Submit")

    if word_submitted:
        if Word_Guess == Solution:
            st.write("Great Success!")
        else:
            st.write("Try again! The solution would have been 'lösung'")
        st.session_state.stage = "done"

if st.session_state.Mistakes == 6:
    st.write("Better luck next time! The correct word was 'lösung'.")