"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    #first player is always X
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making the given move (action) on the board.
    """
    # Validate that the action is within bounds
    if not (0 <= action[0] < 3 and 0 <= action[1] < 3):
        raise ValueError("Action is out of bounds")

    # Validate that the cell is empty
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action: Cell is already occupied")

    # Create a deep copy of the board and apply the action
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    def maximize(board):
        if terminal(board):
            return utility(board), None
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value, _ = minimize(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_value, best_action

    def minimize(board):
        if terminal(board):
            return utility(board), None
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value, _ = maximize(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_value, best_action

    if current_player == X:
        _, action = maximize(board)
    else:
        _, action = minimize(board)

    return action
