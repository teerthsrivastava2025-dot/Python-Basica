import streamlit as st
import random

# Set up the app title and description
st.title("Number Guessing Game")
st.write("Welcome to the number guessing game! Try to guess the correct number.")

# Generate a random number between 1 and 100
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input for guessing
user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100)

# Button to check the guess
if st.button("Check Guess"):
    st.session_state.attempts += 1
    
    if user_guess < st.session_state.number:
        st.write("Your guess is too low. Try again!")
    elif user_guess > st.session_state.number:
        st.write("Your guess is too high. Try again!")
    else:
        st.write(f"Congratulations! You've guessed the correct number {st.session_state.number} in {st.session_state.attempts} attempts!")
        st.session_state.number = random.randint(1, 100)  # Reset the game with a new number

# Option to restart the game
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Game has been restarted! Try to guess the new number.")
