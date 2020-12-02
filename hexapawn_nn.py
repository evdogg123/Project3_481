import copy

INITIAL_BOARD = [[-1,-1,-1],[0,0,0],[1,1,1]]
INITIAL_PLAYER = 1
INITIAL_STATE = (INITIAL_BOARD, INITIAL_PLAYER)

def to_move(state):
    return state[1]


def action(state):
    board = state[0]
    player = state[1]
    moves = []
    forward = player * -1 #Indicates what direction is forward for given player
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                if board[i + forward][j] == 0:
                    moves.append(("advance", i, j))

                if j > 0 and board[i + forward][j - 1] == (-1 * player):
                     moves.append(("capture-left", i, j))
                if  j + 1 < len(board) and board[i + forward][j + 1] == (-1 * player):
                     moves.append(("capture-right", i, j))
    return moves

def result(state, action):
    board, player = state
    forward = player * -1
    temp = copy.deepcopy(board)
    move, i, j = action
    if move == "advance":
        temp[i][j] = 0
        temp[i + forward][j] = player
    if move == "capture-left":
        temp[i][j] = 0
        temp[i + forward][j - 1] = player

    if move == "capture-right":
        temp[i][j] = 0
        temp[i + forward][j + 1] = player

    return (temp, player * -1) #return updated board, flip players turn

def is_terminal(state):
    board, player = state 
    for i in range(len(board)):
        if board[0][i] == 1:
            return (True, 1)
        if board[2][i] == -1:
            return (True, -1)
    
    if not action(state):
        return (True, player*-1)
    
    return (False,0)

def utility(s):
    #Utility for for MAX, simply multiply by -1 for min
    return is_terminal(s)[1]



actions = action(INITIAL_STATE)
print(actions)
state = result(INITIAL_STATE, actions[1])
print(state)
actions = action(state)
print(actions)




