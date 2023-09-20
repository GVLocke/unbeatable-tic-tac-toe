print("Tic tac toe game")
# The original board
# ------------------
#   0   |  X  |   
# ------------------
#       |  X  |    
# ------------------
#    0  |    |    0
# ------------------

original_board = ["O", "X", 2, 3, "X", 5, "O", 7, "O"]
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

print(minmax(original_board, aiPlayer).getIndex())