# Define the board as a list of 9 elements, each representing a square
# The board is indexed as follows:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

# The board can contain 'X', 'O', or '_' (empty)
board = ['_'] * 9

# Define the player symbols
player = 'X'
opponent = 'O'

# Define a function to check if the board is full
def is_full(board):
    return '_' not in board

# Define a function to check if a player has won the game
def is_winner(board, symbol):
    # Check horizontal, vertical, and diagonal lines for a match
    return ((board[0] == board[1] == board[2] == symbol) or # top row
            (board[3] == board[4] == board[5] == symbol) or # middle row
            (board[6] == board[7] == board[8] == symbol) or # bottom row
            (board[0] == board[3] == board[6] == symbol) or # left column
            (board[1] == board[4] == board[7] == symbol) or # middle column
            (board[2] == board[5] == board[8] == symbol) or # right column
            (board[0] == board[4] == board[8] == symbol) or # main diagonal
            (board[2] == board[4] == board[6] == symbol))   # secondary diagonal

# Define a function to evaluate the score of a terminal state
def evaluate(board):
    # If the player wins, return +10
    if is_winner(board, player):
        return 10
    # If the opponent wins, return -10
    elif is_winner(board, opponent):
        return -10
    # If the game is a draw, return 0
    else:
        return 0


#.......................................................................................
# Python3 program to find the next optimal move for a player 
player, opponent = 'X', 'O'

# This function returns true if there are moves 
# remaining on the board. It returns false if 
# there are no moves left to play. 
def isMovesLeft(board) : 

	for i in range(3) : 
		for j in range(3) : 
			if (board[i][j] == '_') : 
				return True
	return False

# This is the evaluation function as discussed 
# in the previous article ( http://goo.gl/sJgv68 ) 
def evaluate(b) : 
	
	# Checking for Rows for X or O victory. 
	for row in range(3) :	 
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :		 
			if (b[row][0] == player) : 
				return 10
			elif (b[row][0] == opponent) : 
				return -10

	# Checking for Columns for X or O victory. 
	for col in range(3) : 
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) : 
		
			if (b[0][col] == player) : 
				return 10
			elif (b[0][col] == opponent) : 
				return -10

	# Checking for Diagonals for X or O victory. 
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) : 
	
		if (b[0][0] == player) : 
			return 10
		elif (b[0][0] == opponent) : 
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) : 
	
		if (b[0][2] == player) : 
			return 10
		elif (b[0][2] == opponent) : 
			return -10

	# Else if none of them have won then return 0 
	return 0

# This is the minimax function. It considers all 
# the possible ways the game can go and returns 
# the value of the board 
def minimax(board, depth, isMax) : 
	score = evaluate(board) 

	# If Maximizer has won the game return his/her 
	# evaluated score 
	if (score == 10) : 
		return score 

	# If Minimizer has won the game return his/her 
	# evaluated score 
	if (score == -10) : 
		return score 

	# If there are no more moves and no winner then 
	# it is a tie 
	if (isMovesLeft(board) == False) : 
		return 0

	# If this maximizer's move 
	if (isMax) :	 
		best = -1000

		# Traverse all cells 
		for i in range(3) :		 
			for j in range(3) : 
			
				# Check if cell is empty 
				if (board[i][j]=='_') : 
				
					# Make the move 
					board[i][j] = player 

					# Call minimax recursively and choose 
					# the maximum value 
					best = max( best, minimax(board, 
											depth + 1, 
											not isMax) ) 

					# Undo the move 
					board[i][j] = '_'
		return best 

	# If this minimizer's move 
	else : 
		best = 1000

		# Traverse all cells 
		for i in range(3) :		 
			for j in range(3) : 
			
				# Check if cell is empty 
				if (board[i][j] == '_') : 
				
					# Make the move 
					board[i][j] = opponent 

					# Call minimax recursively and choose 
					# the minimum value 
					best = min(best, minimax(board, depth + 1, not isMax)) 

					# Undo the move 
					board[i][j] = '_'
		return best 

# This will return the best possible move for the player 
def findBestMove(board) : 
	bestVal = -1000
	bestMove = (-1, -1) 

	# Traverse all cells, evaluate minimax function for 
	# all empty cells. And return the cell with optimal 
	# value. 
	for i in range(3) :	 
		for j in range(3) : 
		
			# Check if cell is empty 
			if (board[i][j] == '_') : 
			
				# Make the move 
				board[i][j] = player 

				# compute evaluation function for this 
				# move. 
				moveVal = minimax(board, 0, False) 

				# Undo the move 
				board[i][j] = '_'

				# If the value of the current move is 
				# more than the best value, then update 
				# best/ 
				if (moveVal > bestVal) :				 
					bestMove = (i, j) 
					bestVal = moveVal 

	# print("The value of the best Move is :", bestVal) 
	# print() 
	return bestMove 
# Driver code 
board = ['_'] * 9

bestMove = findBestMove(board)

def our_need(bestMove):
	if bestMove[0]==0:
		return bestMove[0] + bestMove[1]
	elif bestMove[0]==1:
		return bestMove[0] + bestMove[1] + 2
	else:
		return bestMove[0] + bestMove[1] + 4

print(our_need(bestMove))












# # Define a function to implement the minimax algorithm recursively
# def minimax(board, depth, is_max):
#     # Get the score of the current state
#     score = evaluate(board)

#     # If the score is non-zero, return it as the base case
#     if score != 0:
#         return score

#     # If the board is full, return 0 as the base case
#     if is_full(board):
#         return 0

#     # If it is the player's turn (maximizer), try to maximize the score
#     if is_max:
#         best = -float('inf') # Initialize the best value to negative infinity

#         # Loop through all the empty squares on the board
#         for i in range(9):
#             if board[i] == '_':
#                 # Make a temporary move on the board
#                 board[i] = player

#                 # Recursively call minimax on the next level with the opposite turn
#                 best = max(best, minimax(board, depth + 1, not is_max))

#                 # Undo the temporary move on the board
#                 board[i] = '_'

#         # Return the best value found
#         return best

#     # If it is the opponent's turn (minimizer), try to minimize the score
#     else:
#         best = float('inf') # Initialize the best value to positive infinity

#         # Loop through all the empty squares on the board
#         for i in range(9):
#             if board[i] == '_':
#                 # Make a temporary move on the board
#                 board[i] = opponent

#                 # Recursively call minimax on the next level with the opposite turn
#                 best = min(best, minimax(board, depth + 1, not is_max))

#                 # Undo the temporary move on the board
#                 board[i] = '_'

#         # Return the best value found
#         return best

# # Define a function to find the best possible move for the player using minimax
# def find_best_move(board):
#     best_val = -float('inf') # Initialize the best value to negative infinity
#     best_move = -1           # Initialize the best move to an invalid index

#     # Loop through all the empty squares on the board
#     for i in range(9):
#         if board[i] == '_':
#             # Make a temporary move on the board
#             board[i] = player

#             # Call minimax on the next level with the opponent's turn and get the value
#             move_val = minimax(board, 0, False)

#             # Undo the temporary move on the board
#             board[i] = '_'

#             # If the value of this move is better than the best value, update the best value and the best move
#             if move_val > best_val:
#                 best_val = move_val
#                 best_move = i

#     # Return the best move found
#     print(best_move)
#     return best_move

# Define a function to print the board in a human-readable format
def print_board(board):
    for i in range(3):
        print(board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2])
        if i < 2:
            print('---------')

# Define a function to play the game interactively with the user
def play():
    # Initialize the board to empty
    board = ['_'] * 9

    # Print a welcome message and the instructions
    print('Welcome to Tic-Tac-Toe!')
    print('You are X and the computer is O.')
    print('Enter a number from 0 to 8 to place your mark on the corresponding square.')
    print('The board is indexed as follows:')
    print('0 | 1 | 2')
    print('---------')
    print('3 | 4 | 5')
    print('---------')
    print('6 | 7 | 8')
    print("                       ")
    print("..... Your Board ......")
    print("                       ")
    # Loop until the game is over
    while True:
        # Print the current board
        print_board(board)

        # Get the user's input and validate it
        user_move = int(input('Enter your move: '))
        while user_move < 0 or user_move > 8 or board[user_move] != '_':
            print('Invalid move. Try again.')
            user_move = int(input('Enter your move: '))

        # Make the user's move on the board
        board[user_move] = player

        # Check if the user has won or the game is a draw
        if is_winner(board, player):
            print_board(board)
            print('You win!')
            break
        elif is_full(board):
            print_board(board)
            print('It\'s a draw!')
            break

        # Find the best move for the computer using minimax
        comp_move = find_best_move(board)

        # Make the computer's move on the board
        board[comp_move] = opponent

        # Check if the computer has won or the game is a draw
        if is_winner(board, opponent):
            print_board(board)
            print('You lose!')
            break
        elif is_full(board):
            print_board(board)
            print('It\'s a draw!')
            break

# Call the play function to start the game
play()
