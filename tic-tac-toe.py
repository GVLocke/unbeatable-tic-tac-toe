import time
print("Tic tac toe game")

original_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# human
huPlayer = "O"
# bot
aiPlayer = "X"

class Move:
    """Class that defines each possible move that could be made"""
    def __init__(self, index=None, score=None):
        self.__index = index
        self.__score = score

    def __init__(self, index, score):
        self.__index = index
        self.__score = score

    def getScore(self):
        """Returns the score of the move"""
        return self.__score
    
    def getIndex(self):
        """Returns the index of the move (0-8)"""
        return self.__index
    
    def setScore(self, score):
        self.__score = score

    def setIndex(self, index):
        self.__index = index


# returns a list of empty spots on the board
def emptyIndices(board):
    return [x for x in board if x != "O" and x != "X"]

# winning combinations using the board indices
def winning(board, player):
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False
    
# the main minmax function, baby
def minmax(newBoard, player):
    # get the available spots
    available_spots = emptyIndices(newBoard)

    # checks for terminal states like win, lose, and tie and returns values accordingly
    if winning(newBoard, huPlayer):
        return Move(None, -10)
    elif winning(newBoard, aiPlayer):
        return Move(None, 10)
    elif len(available_spots) == 0:
        return Move(None, 0)
    
    # create a list to store the possible moves
    moves = []

    # loop through available spots
    for i in range(len(available_spots)):
        move = Move(None, None)
        move.setIndex(newBoard[available_spots[i]])

        # set the empty spot to the current player
        newBoard[available_spots[i]] = player

        # collect the score resulted from calling minimax on the opponent of the current player
        if (player == aiPlayer):
            result = minmax(newBoard, huPlayer)
            move.setScore(result.getScore())

        else:
            result = minmax(newBoard, aiPlayer)
            move.setScore(result.getScore())

        # reset the spot to empty
        newBoard[available_spots[i]] = move.getIndex()

        # add the move to the list of moves
        moves.append(move)
    
    # if it is the computer's turn loop over the moves and choose the move with the highest score
    bestMove = None
    if (player == aiPlayer):
        bestScore = -10000
        for i in range(len(moves)):
            if (moves[i].getScore() > bestScore):
                bestScore = moves[i].getScore()
                bestMove = i
    else:
        bestScore = 10000
        for i in range(len(moves)):
            if (moves[i].getScore() < bestScore):
                bestScore = moves[i].getScore()
                bestMove = i

    # return the chosen move object from the moves array
    return moves[bestMove]

# print the board, if the index is an integer, print a space, otherwise print the letter
def printBoard(board):
    print("-------------")
    print("| " + str(board[0] if isinstance(board[0], str) else " ") + " | " + str(board[1] if isinstance(board[1], str) else " ") + " | " + str(board[2] if isinstance(board[2], str) else " ") + " |")
    print("-------------")
    print("| " + str(board[3] if isinstance(board[3], str) else " ") + " | " + str(board[4] if isinstance(board[4], str) else " ") + " | " + str(board[5] if isinstance(board[5], str) else " ") + " |")
    print("-------------")
    print("| " + str(board[6] if isinstance(board[6], str) else " ") + " | " + str(board[7] if isinstance(board[7], str) else " ") + " | " + str(board[8] if isinstance(board[8], str) else " ") + " |")
    print("-------------")

def checkWinner(board):
    if (winning(board, huPlayer)):
        print("You win!")
        return True
    elif (winning(board, aiPlayer)):
        print("You lose!")
        return True
    elif (len(emptyIndices(board)) == 0):
        print("Tie!")
        return True
    else:
        return False

printBoard(original_board)
while 1:
    if (checkWinner(original_board)):
        break
    print("Choose a spot to place your move (0-8)")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    player_move = int(input())
    if (player_move < 0 or player_move > 8):
        print("Invalid move, try again")
        continue
    elif (original_board[player_move] == "O" or original_board[player_move] == "X"):
        print("Invalid move, try again")
        continue
    else:
        original_board[player_move] = huPlayer
    printBoard(original_board)
    if (checkWinner(original_board)):
        break
    startTime = time.time()
    original_board[minmax(original_board, aiPlayer).getIndex()] = aiPlayer
    endTime = time.time()
    print("Computer's move:")
    printBoard(original_board)
    print("Time taken: {:.6f} seconds".format(endTime - startTime))