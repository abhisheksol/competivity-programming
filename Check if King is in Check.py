def is_king_in_check(board, game_num):
    def find_king(board, color):
        for i in range(8):
            for j in range(8):
                if board[i][j].lower() == color:
                    return (i, j)
        return None

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.':
                color = piece.islower()
                if piece.lower() == 'k':
                    king_pos = (i, j)
                    continue
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    while 0 <= ni < 8 and 0 <= nj < 8:
                        if board[ni][nj] != '.':
                            if (color and board[ni][nj].isupper()) or (not color and board[ni][nj].islower()):
                                if (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                    return "Game {}: {} king is in check.".format(game_num, "black" if color else "white")
                            break
                        ni, nj = ni + di, nj + dj
    return "Game {}: no king is in check.".format(game_num)

def main():
    game_num = 0
    while True:
        game_num += 1
        print(f"Enter the configuration for game #{game_num}:")
        board = [input() for _ in range(8)]
        if all(row == '.' * 8 for row in board):
            break
        print(is_king_in_check(board, game_num))

if __name__ == "__main__":
    main()
