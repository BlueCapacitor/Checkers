'''
Created on Mar 10, 2018

@author: gosha
'''

opponent = lambda you : 3 - you


# copies multidimensional lists
def copy_board(board):
    return([list(row) for row in board])


def start():
    board = []
    for y in range(8):
        row = []
        for x in range(8):
            if(y < 3):
                row.append((x + y) % 2)
            elif(y > 4):
                row.append(((x + y) % 2) * 2)
            else:
                row.append(0)
        board.append(row)
    return(board)



def empty():
    return([[0] * 8] * 8)



def print_board(board, labels = False):
    if(labels):
        out = ' ' * 2
        for x in range(8):
            out += ' ' + str(x+1)
        out += '\n ' + '-' * 19 + '\n'
    else:
        out = '-' * 19 + '\n'
    for y in range(8):
        out += (str(y + 1) + '| ') if labels else '| '
        for x in range(8):
            out += ['  ', '1 ', '2 '][board[y][x]]
        out += '|\n'
    out += (' ' + '-' * 19) if labels else ('-' * 19)
    return(out)



# checks the possible moves for a square (Solution for problem 1)
def solution_for_problem_1(board, isWhiteTurn, x, y):
    value = board[y][x]
    
    if(value == 0):
        return("empty")

    if(value == int(isWhiteTurn) + 1):
        return("wrong turn")
    
    # checks for jumps
    moves = check_for_jumps(board, x, y)
    
    if(len(moves) == 0):
        moves = check_for_moves(board, x, y)
    
    return(moves)
    

def check_if_open(board, x, y):
    # check if the square is on the board
    if(y < 0 or y >= 8 or x < 0 or x >= 8):
        return(False)

    # check if the square is empty
    return(board[y][x] == 0)


# checks for jumps
def check_for_jumps(board, x, y):
    
    value = board[y][x]
    moves = []
    
    for JumpX in [-2, 2]:
        JumpY = value * (-4) + 6
        
        if(not(check_if_open(board, JumpX + x, JumpY + y))):
            continue
        
        # checks if the square you are jumping over is an opponent
        if(board[JumpY//2 + y][JumpX//2 + x] == opponent(value)):
            move = copy_board(board)
            move[y][x] = 0
            move[JumpY//2 + y][JumpX//2 + x] = 0
            move[JumpY + y][JumpX + x] = value
            moves.append(move)

    return(moves)


# checks for moves (not jumps)
def check_for_moves(board, x, y):
    
    value = board[y][x]
    moves = []
    
    for MoveX in [-1, 1]:
        MoveY = value * (-2) + 3

        if(not check_if_open(board, MoveX + x, MoveY + y)):
            continue
        
        move = copy_board(board)
        move[y][x] = 0
        move[MoveY + y][MoveX + x] = value
        moves.append(move)
        
    return(moves)



def legalMoves(board, isWhiteTurn):
    
    moves = []
    turn = 2 - int(isWhiteTurn)
    
    # check for jumps
    for y in range(8):
        for x in range(8):
            if(board[y][x] == turn):
                moves += check_for_jumps(board, x, y)
            
    if(len(moves) != 0):
        return(moves)
    
    # check for moves
    for y in range(8):
        for x in range(8):
            if(board[y][x] == turn):
                moves += check_for_moves(board, x, y)
        
    return(moves)



def get_score(board):
    out = 0
    for row in board:
        for cell in row:
            out += (0, 1, -1)[cell]
    return(out)



def find_move(board, isWhiteTurn, depth):
    moves = legalMoves(board, isWhiteTurn)
    
    if(len(moves) == 0):
        return(None, get_score(board) * 100)
        
    if(depth == 0):
        scores = [get_score(move) for move in moves]
    else:
        scores = [find_move(move, not(isWhiteTurn), depth - 1)[1] for move in moves]
        
    bestScore = max(scores) if isWhiteTurn else min(scores)
    i = scores.index(bestScore)
    return((moves[i], bestScore))


def player_move(board, isWhiteTurn):
    possibleMoves = legalMoves(board, isWhiteTurn)
    if(len(possibleMoves) == 0):
        return(None, get_score(board))
    
    # strIn should be in the form of ((x, y), (x2, y2))
    move = raw_input(
'''enter your move in the form of xy x2y2 where you are moving the checker at (x, y) to (x2, y2)
move: ''')
    
    boardCopy = copy_board(board)
   
    try:
        x, y, x2, y2 = int(move[0]) - 1, int(move[1]) - 1, int(move[3]) - 1, int(move[4]) - 1
       
        if(abs(x2 - x) == 1 and abs(y2 - y) == 1):
            boardCopy[y][x] = 0
            boardCopy[y2][x2] = 2 - int(isWhiteTurn)
        
        elif(abs(x2 - x) == 2 and abs(y2 - y) == 2):
            boardCopy[y][x] = 0
            boardCopy[y2][x2] = 2 - int(isWhiteTurn)
            boardCopy[(y + y2) // 2][(x + x2) // 2] = 0
    
        else:
            raise Exception("bad move")
    
        if(boardCopy in possibleMoves):
            return(boardCopy, get_score(boardCopy))
        else:
            raise Exception("bad move")

    except:
        print("please check your move")
        return(player_move(board, isWhiteTurn))
        
    

# =================== UI ==================


def text_UI():
    mode = int(raw_input(
'''Would you like to play
    1: player v. player
    2: player v. CPU
    3: CPU    v. CPU
answer: '''))
    if(mode != 1):
        CPULevel = int(raw_input(
'''select CPU level 0 - 6 (the CPU level is the number of steps it will look ahead)
answer: '''))
        
    if(mode == 3):
        CPUvCPU(CPULevel)
    elif(mode == 2):
        PvCPU(CPULevel)
    elif(mode == 1):
        PvP()
        
    

def CPUvCPU(level = 5):
    board = start()
    turn = True
    while True:
        print(print_board(board))
        move = find_move(board, turn, level)
        board = move[0]
        
        if(check_for_end(move)):
            break
        turn = not(turn)
        

def PvCPU(level = 5):
    board = start()
    turn = True
    while True:
        print(print_board(board, True))
        if(turn):
            move = find_move(board, turn, level)            
        else:
            move = player_move(board, turn)
        board = move[0]
        
        if(check_for_end(move)):
            break
        turn = not(turn)
        

def PvP():
    board = start()
    turn = True
    while True:
        print(print_board(board, True))
        
        print("it is " + str(1 + int(not(turn))) + "'s turn")
        move = player_move(board, turn)
        board = move[0]

        if(check_for_end(move)):
            break
        turn = not(turn)


def check_for_end(move):
    board, score = move
        
    if(board == None):
        if(score == 0):
            print("Draw")
        else:
            print(("White" if score > 0 else "Black") + " wins")
        return(True)
    print(score)
    return(False)

if __name__ == '__main__':
    text_UI()