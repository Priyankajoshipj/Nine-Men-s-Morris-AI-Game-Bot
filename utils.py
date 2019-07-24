
from copy import deepcopy
def generateAdd(boardposition):
    galist=[]
    for i in range(len(boardposition)):
        if boardposition[i]=='x':
            boardcopy=deepcopy(boardposition)
            boardcopy[i]='W'
            if closeMill(i,boardcopy):
                galist=generateRemove(boardcopy,galist)
            else:
                galist.append(boardcopy)
    
    return galist

def possibleNextMill(position, board, player): 
     
    mill = [
        (isSamePlayer(player, board, 8, 20) or isSamePlayer(player, board, 1, 2) or isSamePlayer(player, board, 3, 6)),
        (isSamePlayer(player, board, 0, 2)),
        (isSamePlayer(player, board, 0, 1) or isSamePlayer(player, board, 5, 7) or isSamePlayer(player, board, 13, 22)),
        (isSamePlayer(player, board, 9, 17) or isSamePlayer(player, board, 0, 6) or isSamePlayer(player, board, 4, 5)),
        (isSamePlayer(player, board, 3, 5)),
        (isSamePlayer(player, board, 3,4) or isSamePlayer(player, board, 2, 7) or isSamePlayer(player, board, 12, 19)),
        (isSamePlayer(player, board, 10, 14) or isSamePlayer(player, board, 0, 3)),
        (isSamePlayer(player, board, 11, 16) or isSamePlayer(player, board, 2, 5)),
        (isSamePlayer(player, board, 9, 10) or isSamePlayer(player, board, 0, 20)),
        (isSamePlayer(player, board, 3, 17) or isSamePlayer(player, board, 8, 10)),
        (isSamePlayer(player, board, 6, 14) or isSamePlayer(player, board, 8, 9)),
        (isSamePlayer(player, board, 7, 16) or isSamePlayer(player, board, 12, 13)),
        (isSamePlayer(player, board, 11, 13) or isSamePlayer(player, board, 5, 19)),       
        (isSamePlayer(player, board, 2, 22) or isSamePlayer(player, board, 11, 12)),        
        (isSamePlayer(player, board, 15, 16) or isSamePlayer(player, board, 17, 20) or isSamePlayer(player, board, 6, 10)),
        (isSamePlayer(player, board, 14, 16) or isSamePlayer(player, board, 21, 18)),
        (isSamePlayer(player, board, 11, 7) or isSamePlayer(player, board, 14, 15) or isSamePlayer(player, board, 19, 22)),
        (isSamePlayer(player, board, 9, 3) or isSamePlayer(player, board, 18, 19) or isSamePlayer(player, board, 14, 20)),
        (isSamePlayer(player, board, 21, 15) or isSamePlayer(player, board, 17, 19)),
        (isSamePlayer(player, board, 17, 18) or isSamePlayer(player, board, 12, 5) or isSamePlayer(player, board, 16, 22)),
        (isSamePlayer(player, board, 0, 8) or isSamePlayer(player, board, 21, 22) or isSamePlayer(player, board, 14, 17)),
        (isSamePlayer(player, board, 20, 22) or isSamePlayer(player, board, 18, 15)),
        (isSamePlayer(player, board, 20, 21) or isSamePlayer(player, board, 2, 13) or isSamePlayer(player, board, 16, 19)),
    ]

    return mill[position]
def isSamePlayer(player, board, p1, p2):
    if (board[p1] == player and board[p2] == player):
        return True
    else:
        return False
def closeMill(position, board):
    p = board[position]
    # The player on that position
    if p != 'x':
        # If there is some player on that position
        return possibleNextMill(position, board, p)
    else:
        return False
def generateRemove(boardposition,l):
    lCopy=deepcopy(l)
    for loc in range(len(boardposition)):
        if boardposition[loc]=='B':
            if (not closeMill(loc, boardposition)):
                boardCopy = deepcopy(boardposition)
                boardCopy[loc] = 'x'
                lCopy.append(boardCopy)
            else:
                boardCopy = deepcopy(boardposition)
                lCopy.append(boardCopy)
    return lCopy
def staticEstimation(board,gamestate):
    numWhitePieces=0
    numBlackPieces=0
    blackmoveslist=generateBlackMoves(board)
    numBlackMoves=len(blackmoveslist)
    for loc in board:
        if loc == 'W':
            numWhitePieces+=1
        if loc == 'B':
            numBlackPieces+=1
    if(gamestate=='MidgameEndgame'):
        if (numBlackPieces <= 2):
            return 10000
        elif (numWhitePieces <= 2):
            return -10000
        elif (numBlackMoves==0):
            return 10000
        else:
            return ( 1000*(numWhitePieces - numBlackPieces) - numBlackMoves)
    if(gamestate=='Opening'):
        return (numWhitePieces - numBlackPieces)

def generateInvertedBoardList(pos_list):
    '''
    '''
    result = []
    for i in pos_list:
        if i == "W":
            result.append("B")
        elif i == "B":
            result.append("W")
        else:
            result.append('x')
    return result
def generateBlackMoves(boardposition):
    copy=deepcopy(boardposition)
    invertedcopy=generateInvertedBoardList(copy)
    newpos=generateAdd(invertedcopy)
    reverted=[]
    for new in newpos:
        reverted.append(generateInvertedBoardList(new))
    return reverted
def generateHopping(boardposition):
    l=[]
    for i in range(len(boardposition)):
        if boardposition[i]=='W':
            for j in range(len(boardposition)):
                if boardposition[j]=='x':
                    boardCopy=deepcopy(boardposition)
                    boardCopy[i]='x'
                    boardCopy[j]='W'
                    if closeMill(j,boardCopy):
                        l = generateRemove(boardCopy, l)
                    else:
                        l.append(boardCopy)
    return l
def generateMovesMidgameEndgame(boardposition):
    l=[]
    numWhitePieces=0
    for i in range(len(boardposition)):
        if boardposition[i]=='W':
            numWhitePieces+=1
    if(numWhitePieces==3):
        l=generateHopping(boardposition)
        return l
    else:
        l=generateMove(boardposition)
        return l
def generateMove(boardposition):
    l=[]
    boardCopy=deepcopy(boardposition) #do a deep copy
    for i in range(len(boardposition)):
        if boardposition[i]=='W':
            nlist=neighbors(i)
            for n in nlist:
                if boardposition[n]=='x':
                    boardCopy=deepcopy(boardposition)
                    boardCopy[i]='x'
                    boardCopy[n]='W'
                    if closeMill(n,boardCopy):
                        l = generateRemove(boardCopy, l)
                    else:
                        l.append(boardCopy)
    return l
def neighbors(position):
    listofneighbors = {
        0: [1,3,8],
        1: [0,2,4],
        2: [1,5,13],
        3: [0,4,6,9],
        4: [1,3,5],
        5: [2,4,7,12],
        6: [3,7,10],
        7: [5,6,11],
        8: [0,9,20],
        9: [3,8,10,17],
        10: [6,9,14],
        11: [7,12,16],
        12: [5,11,13,19],
        13: [2,12,22],
        14: [10,15,17],
        15: [14,16,18],
        16: [11,15,19],
        17: [9,14,18,20],
        18: [15,17,19,21],
        19: [12,16,18,22],
        20: [8,17,21],
        21: [18,20,22],
        22: [13,19,21]
    }
    return listofneighbors[position]
def printBoard(board):
    print(board[20] + "(20)----------------------" + board[21] +
          "(21)----------------------" + board[22] + "(22)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + board[17] + "(17)--------------" +
          board[18] + "(18)--------------" + board[19] + "(19)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + board[14] + "(14)-----" +
          board[15] + "(15)-----" + board[16] + "(16)       |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[8] + "(08)---" + board[9] + "(09)----" + board[10] + "(10)               " +
          board[11] + "(11)----" + board[12] + "(12)---" + board[13] + "(13)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + board[6] + "(06)-----" +
          "-----------" + board[7] + "(07)      |      |")
    print("|       |                                        |      |")
    print("|       |                                        |      |")
    print("|       |                                        |      |")
    print("|       " + board[3] + "(03)--------------" +
          board[4] + "(04)--------------" + board[5] + "(05)     |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(board[0] + "(00)----------------------" + board[1] +
          "(01)----------------------" + board[2] + "(02)")
    print("\n")