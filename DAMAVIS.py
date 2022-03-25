import operator

def move(s, x):
    s1 = []
    s1.append([x[0],x[1]])
    for i in range(len(s)):
        s1.append(s[i])
    return(s1)

def availablesteps(s, rl, cl):
    up = [s[0][0], s[0][1]+1]
    right = [s[0][0]+1, s[0][1]]
    left = [s[0][0]-1, s[0][1]]
    down = [s[0][0], s[0][1]-1]
    mvs = [up, right, left, down]
    s.pop(-1)
    pops = []
    for i in range(len(mvs)):
        if(not(0<=mvs[i][0]<rl) or not(0<=mvs[i][1]<cl) or (mvs[i] in s)):
            mvs[i] = 'X'
    mvs = [x for x in mvs if x != 'X']
    return(mvs)

def paths(s, n, m, d):
    steps = availablesteps(s, n, m)
    print(s)
    print(steps)
    if d == 1:
        return(len(steps))
    else:
        npaths = 0
        d = d-1
        for i in range(len(steps)):
            s1 = move(s, steps[i])
            npaths = npaths + paths(s1, n, m, d)
        return(npaths)

#Test 1
# board = [3, 4]
# n = board[0]
# m = board[1]
# snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
# depth = 3

#Test 2
# board = [2, 3]
# n = board[0]
# m = board[1]
# snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
# depth = 10

# Test 3
board = [10, 10]
n = board[0]
m = board[1]
snake = [[5,5], [5,4], [4,4], [4,5]]
depth = 4

# Board Constraints
if (len(board) != 2):
    raise Exception("Length of board must be 2")
if (not(1<=n<=10) or not(1<=m<=10)):
    raise Exception("Board rows and columns must be between 1 and 10, both included")

# Snake Constraints
if (not(3<=len(snake)<=10)):
    raise Exception("Length of snake must be between 3 and 7, both included")
for i in range(0, len(snake)):
    if (len(snake[i]) != 2):
        raise Exception("Length of snake parts coordinates must be 2")
    if (not(0<=snake[i][0]<=n) or not(0<=snake[i][1]<=m)):
        raise Exception("Snake rows coordinates must be between 0 and "+str(n)+"\nSnake columns coordinates must be between 0 and "+str(m))
    # Snake Coherence
    if (i != 0):
        if(not(operator.xor(not(snake[i][0] == snake[i-1][0]), not(snake[i][1] == snake[i-1][1])))):
            raise Exception("The snake parts mast be contiguous")
    
# Depth constraints
if (not(1<depth<20)):
    raise Exception("Depth must be between 1 and 20, both included")

print(paths(snake, n, m, depth))