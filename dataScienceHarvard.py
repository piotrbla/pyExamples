import matplotlib.pyplot as plt
import numpy as np
import time


def plot_fun():
    plt.plot([1, 2, 4, 9, 12, 16], "r1-", markersize=15)
    plt.show()


def log_plot():
    x = np.logspace(0, 1, 10)
    y = x ** 2
    plt.loglog(x, y, "bo-")
    plt.subplot(3, 3, 3)
    plt.show()


def create_board():
    return np.zeros((3, 3))


def place(board, player, position):
    board[position[0]][position[1]] = player


def possibilities(board):
    return np.where(board == 0)


def random_place(board, player):
    x = possibilities(board)
    z = np.random.choice(x[0])
    board[z][z] = player
    return board


def row_win(board, player):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] == player:
            return True
    return False


def col_win(board, player):
    for col in board.T:
        if col[0] == col[1] and col[1] == col[2] and col[0] == player:
            return True
    return False


def diag_win(board, player):
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0):
        winner = -1
    return winner


def play_game():
    board = create_board()
    while evaluate(board) == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            if evaluate(board) != 0:
                break


def main():
    board = create_board()
    place(board, 1, (0, 0))
    board = random_place(board, 2)
    # log_plot()
    print(board)
    print(row_win(board, 1))
    print(col_win(board, 1))
    print(diag_win(board, 1))
    start = time.time()
    results = []
    for i in range(1000):
        results.append(play_game())
    stop = time.time()
    print(stop - start)
    plt.hist(results)
    plt.show()

if __name__ == '__main__':
    main()
