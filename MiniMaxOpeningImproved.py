from utils import *
from copy import deepcopy
import sys

class MiniMaxOpeningImproved:
    POSITIONS_EVALUATED=0
    MINIMAX_ESTIMATE=0
    def MinMax(self,boardpositions,depth,gamestate):
        if(depth>0):
            depth-=1
            bchildren=generateBlackMoves(boardpositions)
            v=999999
            minboardchoice=[]
            for j in range(len(bchildren)):
                maxboard=self.MaxMin(bchildren[j],depth,gamestate)
                if(v>self.staticEstimation(maxboard,gamestate)):
                    v=self.staticEstimation(maxboard,gamestate)
                    self.MINIMAX_ESTIMATE =v
                    minboardchoice=bchildren[j]
            return minboardchoice
        elif(depth==0):
            self.POSITIONS_EVALUATED+=1
        return boardpositions
    def staticEstimation(self,board,gamestate):
        numWhitePieces=0
        numBlackPieces=0
        blackmoveslist=generateBlackMoves(board)
        numBlackMoves=len(blackmoveslist)
        for loc in board:
            if loc == 'W':
                numWhitePieces+=1
            if loc == 'B':
                numBlackPieces+=1
            return (numBlackMoves)
    def MaxMin(self,boardpositions,depth,gamestate):
        if(depth>0):
            depth-=1
            if(gamestate=='Opening'):
                children=generateAdd(boardpositions)
            elif(gamestate=='MidgameEndgame'):
                children=generateMovesMidgameEndgame(boardpositions)
            v=-999999
            maxboardchoice=[]
            for j in range(len(children)):
                minboard=self.MinMax(children[j],depth,gamestate)
                if(v<self.staticEstimation(minboard,gamestate)):
                    v=self.staticEstimation(minboard,gamestate)
                    self.MINIMAX_ESTIMATE =v
                    maxboardchoice=children[j]
            return maxboardchoice
        elif(depth==0):
            self.POSITIONS_EVALUATED+=1
        return boardpositions


if __name__ == "__main__":
    print("----------MiniMaxOpeningImproved----------")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    depth = int(sys.argv[3])
    with open(input_file,'r') as i:
        lines = i.readlines()
        board_input=lines[0]
        board_list = list(board_input)
        m = MiniMaxOpeningImproved()
        print("Given Board:", board_input)
        printBoard(board_input)
        d = m.MaxMin(board_list, int(depth),'Opening')
        print("Board position:", "".join(d))
        print("Positions Evaluated by Static Estimation: ", m.POSITIONS_EVALUATED)
        print("Minimax Estimate:", m.MINIMAX_ESTIMATE)
        printBoard(d)
        with open(output_file,'a+') as o:
            o.write("".join(d)+"\n")

    o.close()
    i.close()
