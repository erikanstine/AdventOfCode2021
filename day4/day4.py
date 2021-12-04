def process_boards(boards_raw):
    all_lines = [l for l in boards_raw if l != '\n']
    processed_boards = []
    for i in range(0, len(all_lines), 5):
        new_board = all_lines[i:i+5]
        new_board = [[n for n in l.strip().split(' ') if n] for l in new_board]
        processed_boards.append(new_board)
    return processed_boards

def load_input(fn):
    boards_raw = []
    with open(fn, 'r') as f:
        numbers = [n.strip() for n in f.readline().split(',')]
        boards_raw = f.readlines()
    return numbers, process_boards(boards_raw)

# If num in board, change position to 'X'
def update_board(n, board):
    new_board = board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                new_board[i][j] = 'X'
    return new_board


# Check if board 'wins'
def check_board(board):
    if board == 'DONE':
        return False
    for row in board:
        if all([char == 'X' for char in row]):
            return True
    for col in range(len(board[0])):
        if all([char == 'X' for char in [r[col] for r in board]]):
            return True

    return False

def calculate_score(n, b):
    flat_list = [i for s in b for i in s]
    print(flat_list)
    nums = [int(c) for c in flat_list if c != 'X']
    print(nums)
    remaining = sum(nums)
    print(remaining)
    print(int(n))
    return  remaining * int(n)

def play_bingo(numbers, boards):
    for n in numbers:
        print('Number drawn: ', n)
        for i in range(len(boards)):
            boards[i] = update_board(n, boards[i])
            if check_board(boards[i]):
                score = calculate_score(n, boards[i])
                print('WINNER!\nScore: ', score)
                return True
    print('No winning board')
    return False

def lose_bingo(numbers, boards):
    for n in numbers:
        for i in range(len(boards)):
            boards[i] = update_board(n, boards[i])
            if check_board(boards[i]):
                score = calculate_score(n, boards[i])
                print('Board #{} wins!'.format(i+1))
                if len([b for b in boards if b != 'DONE']) == 1:
                    print('Last to win score: ', score)
                boards[i] = 'DONE'
    return False

if __name__ == "__main__":
    n, b = load_input('day4.txt')
    #n, b = load_input('day4-test.txt')
    #print('Numbers: ', n)
    #print('Boards: ', b)
    #play_bingo(n, b)
    lose_bingo(n, b)
    #print(calculate_score(n[0], b[0]))
