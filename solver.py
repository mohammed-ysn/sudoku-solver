def display_board(board):
    # Iterate through the rows
    for row in range(len(board)):
        # Print horizontal line every third row except the last
        if row % 3 == 0 and row != 0:
            print('-' * 21)

        # Iterate through the numbers in the row
        for col in range(len(board[0])):
            # Print vertical line every third number except the last
            if col % 3 == 0 and col != 0:
                print('| ', end='')

            if col != 8:
                # Print the number
                print(str(board[row][col]) + ' ', end='')
            else:
                # Print the number and a new line
                print(board[row][col])


def find_blank(board):
    # Iterate through all spaces until an empty one is found
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return {
                    "row": row,
                    "col": col
                }

    # Board is full
    return None


def is_valid(board, num, pos):
    # Check for the same number is in the row
    for col in range(len(board[0])):
        if (board[pos["row"]][col] == num) and (col != pos["col"]):
            return False

    # Check for the same number is in the column
    for row in range(len(board)):
        if (board[row][pos["col"]] == num) and (row != pos["row"]):
            return False

    # Locate which region the square is in
    region = {
        "x": pos["col"] // 3,
        "y": pos["row"] // 3
    }

    # Check for the same number in the region
    for row in range((region["y"] * 3), (region["y"] * 3 + 3)):
        for col in range((region["x"] * 3), (region["x"] * 3 + 3)):
            if (board[row][col] == num) and (row != pos["row"]) and (col != pos["col"]):
                return False

    # Number is not present in its row, column or region
    return True


def solve(board):
    # Find a blank square
    blank_pos = find_blank(board)

    # If there are no blank squares the puzzle is solved
    if not blank_pos:
        return True

    # Try numbers 1 to 10 in the blank square
    for num in range(1, 10):
        if is_valid(board, num, blank_pos):
            # Set the squares value to the current number
            board[blank_pos["row"]][blank_pos["col"]] = num

            # Puzzle is solved
            if solve(board):
                return True

            # Reset the square as the current number is invalid
            board[blank_pos["row"]][blank_pos["col"]] = 0

    # Invalid solution
    return False


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solve(board)

    display_board(board)


if __name__ == "__main__":
    main()
