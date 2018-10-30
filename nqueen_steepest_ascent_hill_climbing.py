import random

def get_random_board(n):
    board = []
    for i in range(0, n):
        row = random.randint(0, n - 1)
        board.append(row)
    return board


def count_conflicts(board):
    n = len(board)
    row =[0]*n
    diagonal = [0]*(2*n)
    inverse_diagonal = [0]*(2*n)
    total_conflicts = 0
    for i in range(0,n):
        total_conflicts += row[board[i]]
        total_conflicts += diagonal[i - board[i] + n]
        total_conflicts += inverse_diagonal[i + board[i]+1]
        diagonal[i - board[i] + n] = 1
        row[board[i]] = 1
        inverse_diagonal[i + board[i]+1] = 1
    return total_conflicts


def get_next_board(board):
    better_board = []
    least_conflicts = count_conflicts(board)
    for c in range(0, len(board)):
        current_row = board[c]
        for r in range(0, len(board)):
            board[c] = r
            new_conflicts = count_conflicts(board)
            if new_conflicts <= least_conflicts:
                least_conflicts = new_conflicts
                better_board = list(board)
        board[c] = current_row
    return better_board, least_conflicts

n = 100
board = get_random_board(n)
cnt = 0
best_board = list(board)
least_conflicts = count_conflicts(best_board)
shoulder = 0
final_conflicts = least_conflicts
final_board = list(board)

print("Initial board: ", board, " Conflicts: ", least_conflicts)

while True:
    next_board, conflicts = get_next_board(best_board)
    if conflicts == 0:
       best_board = list(next_board)
       least_conflicts = conflicts
       break

    if conflicts < final_conflicts:
        final_conflicts = conflicts
        final_board = list(next_board)
    
    if conflicts < least_conflicts:
        least_conflicts = conflicts
        best_board = list(next_board)
        
    elif conflicts == least_conflicts and shoulder < 100:
        print(shoulder)
        shoulder += 1
        best_board = list(next_board)
        
        
    elif cnt <= 10:
        best_board = get_random_board(n)
        cnt +=1
        least_conflicts = count_conflicts(best_board)
        shoulder = 0
    else:
        break

print("Best board: ", final_board, " Conflicts: ", final_conflicts)
