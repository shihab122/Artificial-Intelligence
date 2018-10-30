import random
import math

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
    next_board = []
    
    c = random.randint(0, len(board) - 1)
    while True:
        r = random.randint(0, len(board) - 1)
        if board[c] != r:
            break;
    next_board = list(board)
    next_board[c] = r

    conflicts = count_conflicts(next_board)
    return next_board, conflicts


board = get_random_board(500)

best_board = list(board)
E1 = count_conflicts(best_board)
print("Initial board: ", board, " Conflicts: ", E1)
final_board = list(board)
final_conflicts = E1

T = 100.0
cooling_rate = 0.00001

while T>=.000000000000001:
    next_board, E2 = get_next_board(best_board)
    
    if final_conflicts == 0:
        break;
    
    if final_conflicts >= E2:
        print("Conflicts: ",E2)
        final_conflicts = E2
        final_board = list(next_board)

    if E2 <= E1:
        E1 = E2
        best_board = list(next_board)
        
    else:
        rnd = random.uniform(0, 1)
        difference = (E1 - E2)/T
        difference = math.exp(difference)
        
        if rnd < difference:
            E1 = E2
            best_board = list(next_board)
        else:
            best_board = list(final_board)
            E1 = final_conflicts
    T = T - cooling_rate

print("Final Board: ",final_board," Conflicts: ",final_conflicts)
