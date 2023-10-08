squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

EMPTY = "-"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
PAWN = "PAWN"

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print(board)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

board[4][2] = KNIGHT
board[3][4] = PAWN

print(board)

# [expression for element in list if conditional]

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]


odded_divided_3 = [number * 1 for number in range(11)]
print(odded_divided_3)
