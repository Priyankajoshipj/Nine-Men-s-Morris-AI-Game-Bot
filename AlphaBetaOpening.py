from utils import *
from copy import deepcopy
import sys
class AlphaBetaOpening:
    POSITIONS_EVALUATED=0
    ALPHABETA_ESTIMATE=0
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
    print("----------AlphaBetaOpening----------")
    depth = sys.argv[3]
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file,'r') as i:
        lines = i.readlines()
        board_input=lines[0]
        board_list = list(board_input)
        x=-999999
        y=999999
        printBoard(board_list)
        ab = AlphaBetaOpening()
        print("Given Board:", board_input)
        d = ab.MaxMin(board_list, int(depth),'Opening',x,y)
        print("Board position:", "".join(d))
        print("Positions Evaluated by Static Estimation: ", ab.POSITIONS_EVALUATED)
        print("Alpha Beta Estimate:", ab.ALPHABETA_ESTIMATE)
        printBoard(d)
        with open(output_file,'a+') as o:
                o.write("".join(d)+"\n")

        o.close()
        i.close()