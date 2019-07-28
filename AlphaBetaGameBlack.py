from utils import *
from copy import deepcopy
import sys
class AlphaBetaGameBlack:
    POSITIONS_EVALUATED=0
    MINIMAX_ESTIMATE=0
    def MinMax(self,boardpositions,depth,gamestate,alpha,beta):
        if(depth>0):
            depth-=1
            bchildren=generateBlackMoves(boardpositions)
            v=999999
            minboardchoice=[]
            for j in range(len(bchildren)):
                maxboard=self.MaxMin(bchildren[j],depth,gamestate,alpha,beta)
                if(v>staticEstimation(maxboard,gamestate)):
                    v=staticEstimation(maxboard,gamestate)
                    self.ALPHABETA_ESTIMATE =v
                    minboardchoice=bchildren[j]
                if(v<=alpha):
                    return minboardchoice
                else:
                    beta = min(v,beta)
            return minboardchoice
        elif(depth==0):
            self.POSITIONS_EVALUATED+=1
        return boardpositions

    def MaxMin(self,boardpositions,depth,gamestate,alpha,beta):
        if(depth>0):
            depth-=1
            if(gamestate=='Opening'):
                children=generateAdd(boardpositions)
            elif(gamestate=='MidgameEndgame'):
                children=generateMovesMidgameEndgame(boardpositions)
            v=-999999
            maxboardchoice=[]
            for j in range(len(children)):
                minboard=self.MinMax(children[j],depth,gamestate,alpha,beta)
                if(v<staticEstimation(minboard,gamestate)):
                    v=staticEstimation(minboard,gamestate)
                    self.ALPHABETA_ESTIMATE =v
                    maxboardchoice=children[j]
                if(v>=beta):
                    return maxboardchoice
                else:
                    alpha = max(v,alpha)
            return maxboardchoice
        elif(depth==0):
            self.POSITIONS_EVALUATED+=1
        return boardpositions




if __name__ == "__main__":
    print("----------AlphaBetaGameBlack----------")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    depth = int(sys.argv[3])
    with open(input_file,'r') as i:
        lines = i.readlines()
        board_input=lines[0]
        board_list = list(board_input)
        m = AlphaBetaGameBlack()
        x=-999999
        y=999999
        print("Given Board:", board_input)
        printBoard(board_input)
        invertedforblack=generateInvertedBoardList(board_input)
        nextmove = m.MaxMin(invertedforblack, int(depth),'MidgameEndgame',x,y)
        boardToDisplay=generateInvertedBoardList(nextmove)
        print("Board position:", "".join(boardToDisplay))
        print("Positions Evaluated by Static Estimation: ", m.POSITIONS_EVALUATED)
        print("Minimax Estimate:", m.MINIMAX_ESTIMATE)
        printBoard(boardToDisplay)
        with open(output_file,'a+') as o:
            o.write("Move White -> "+"".join(board_input)+"\n")
            o.write("Move Black "+"".join(boardToDisplay)+"\n")

    o.close()
    i.close()
