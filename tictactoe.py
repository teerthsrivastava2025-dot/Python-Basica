import streamlit as st

# Function to initialize the game board
def init_game():
    return [[" " for _ in range(3)] for _ in range(3)], "X", 0

# Function to check if someone has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

# Game UI
st.title("Tic Tac Toe")

# Initialize game state if not already initialized
if 'board' not in st.session_state:
    st.session_state.board, st.session_state.current_player, st.session_state.turns = init_game()

# Function to render the board
def render_board(board):
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            cols[j].button(board[i][j], key=f"{i}-{j}", on_click=handle_click, args=(i, j))

# Function to handle player's click
def handle_click(i, j):
    # Check if the cell is empty
    if st.session_state.board[i][j] == " ":
        st.session_state.board[i][j] = st.session_state.current_player
        if check_winner(st.session_state.board, st.session_state.current_player):
            st.session_state.game_over = True
            st.success(f"Player {st.session_state.current_player} wins!")
        elif check_draw(st.session_state.board):
            st.session_state.game_over = True
            st.warning("It's a draw!")
        else:
            # Switch player
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            st.session_state.turns += 1

# Display the board
render_board(st.session_state.board)

# Display whose turn it is
if not hasattr(st.session_state, 'game_over') or not st.session_state.game_over:
    st.write(f"Player {st.session_state.current_player}'s turn")
else:
    # Option to restart the game
    if st.button("Restart Game"):
        st.session_state.board, st.session_state.current_player, st.session_state.turns = init_game()
        st.session_state.game_over = False
