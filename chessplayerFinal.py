from random import *
class heap:
    def __init__(self):
        self.data=[]
        self.open=0

    def reheap(self,child):
        parent=int((child-1)/2)
        if (self.data[child]>self.data[parent]):
            temp=self.data[child]
            self.data[child]=self.data[parent]
            self.data[parent]=temp
            self.reheap(parent)
            return True
        else:
            return True

    def add(self, value):
         self.data[self.open]=value
         self.reheap(self.open)
         self.open+=1
         return True

    def extract(self):
         value=self.data[1]
         self.data[1]=self.data[self.open-1]
         self.open=self.open-1
         for i in range(2,self.open,1):
             self.reheap(i)
         return value

class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        value = self.data[len(self.data) - 1]
        self.data = self.data[0:len(self.data) - 1]
        return value

    def push(self, data):
        self.data += [data]
        return True

    def clearstack(self):
        self.data = []
        return True

    def getdata(self, index):
        return self.data[index]

class queue:
    def __init__(self):
        self.data = []
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        self.data = self.data + [data]
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return False
        value = self.data[0]
        self.data = self.data[1:]
        self.size = self.size - 1
        return value

    def getsize(self):
        return self.size

class chess:
    def __init__(self):
        self.master=[]
        self.pieces=[]

    def genEmptyBoard(self):
        #making an empty int board to calculate moves. pawns are worth 2 and whites are offset by 10 while black by 20
        for j in range (0,64,1):
            self.pieces=self.pieces+[0]
            if j>7 and j<16:
                self.pieces[j]=10
            if j<56 and j>47:
                self.pieces[j]=20

        #assigning values to the starting pieces. Each piece is worth a different amount
        self.pieces[0],self.pieces[7]=13,13
        self.pieces[1],self.pieces[6]=11,11
        self.pieces[2],self.pieces[5]=12,12
        self.pieces[3]=14
        self.pieces[4]=15

        self.pieces[63], self.pieces[56] = 23,23
        self.pieces[62], self.pieces[57] = 21,21
        self.pieces[61], self.pieces[58] = 22,22
        self.pieces[59] = 24
        self.pieces[60] = 25
        return True

    def makeUserBoard(self):
        self.master=[]
        #making an empty board for the user to see. # is white. _ is black
        for i in range(2 ,10 ,1):
            if i % 2 == 0:
                self.master = self.master+self.genEven()
            else:
                self.master = self.master+self.genOdd()
        #mapping the board the user can look at to the integer board
        for i in range (0,64,1):
            if self.pieces[i]==10:
                self.master[i]='p '
            if self.pieces[i]==20:
                self.master[i]='p*'
            if self.pieces[i]==13:
                self.master[i]='r '
            if self.pieces[i]==11:
                self.master[i]='k '
            if self.pieces[i]==12:
                self.master[i]='b '
            if self.pieces[i]==14:
                self.master[i]='Q '
            if self.pieces[i]==15:
                self.master[i]="K "
            if self.pieces[i]==23:
                self.master[i]='r*'
            if self.pieces[i]==21:
                self.master[i]='k*'
            if self.pieces[i]==22:
                self.master[i]='b*'
            if self.pieces[i]==24:
                self.master[i]='Q*'
            if self.pieces[i]==25:
                self.master[i]="K*"
        return True

    def genOdd(self):
        list1=['# ','_ ','# ','_ ','# ','_ ','# ','_ ']
        return list1

    def genEven(self):
        list1=['_ ','# ','_ ','# ','_ ','# ','_ ','# ']
        return list1

    def printBoard(self):
        list1=[]
        for i in range (0,64,1):
            list1=list1+[i]
        print("row 0 ",self.master[0:8], "  ", list1[0:8])
        print("row 1 ",self.master[8:16], "  ", list1[8:16])
        print("row 2 ",self.master[16:24], "  ", list1[16:24])
        print("row 3 ",self.master[24:32], "  ", list1[24:32])
        print("row 4 ",self.master[32:40], "  ", list1[32:40])
        print("row 5 ",self.master[40:48], "  ", list1[40:48])
        print("row 6 ",self.master[48:56], "  ", list1[48:56])
        print("row 7 ",self.master[56:64], "  ", list1[56:64])
        return True

    def GetPlayerPositions(self,board1,player):
        board=[]
        board=board+board1
        list1ofpos=[]
        for i in range(0,64,1):
            if player==20:
                if board[i]>=20:
                    list1ofpos=list1ofpos+[i]
            if player==10:
                if board[i]<20 and board[i]>0:
                    list1ofpos=list1ofpos+[i]
        return list1ofpos

    def GetPieceLegalMoves(self,board1,position):
        board=[]
        board=board+board1
        list1=[]
        player=0
        if board[position]>=10 and board[position]<18:
            player=10
        if board[position]>=20 and board[position]<28:
            player=20
        if board[position]==0:
            return [False]
        piece=board[position]-player
        h = self.horizlist1(position, player)
        x = self.verticallist1(position, player)
        d = self.diaglist1(position, player)
        if piece==4:
            list1=list1+d+h+x
        if piece==2:
            list1=list1+d
        if piece==3:
            list1=list1+h+x

        #if pawn
        if piece==0:
            if player==20:
                factor=-1
            if player==10:
                factor=1
            if position+(factor*8)<64 and position+(factor*8)>=0:
                if board[position+(factor*8)]==0:
                    list1=list1+[position+(factor*8)]
            if (position+factor*9<64 and position+factor*9>=0):
                if board[position+factor*9]!=0:
                    if player==20 and board[position+factor*9]<20 and position%8!=0:
                        list1=list1+[position+factor*9]
                    if player==10 and board[position+factor*9]>=20 and (position+factor*9)%8!=0:
                        list1=list1+[position+factor*9]
            if (position+factor*7<64 and position+factor*7>=0):
                if board[position+factor*7]!=0:
                    if (player == 20 and board[position + factor * 7] < 20 and position%8!=0):
                        list1 = list1 + [position + factor * 7]
                    if player == 10 and board[position + factor * 7] >= 20 and (position+factor*7)%8!=0:
                        list1 = list1 + [position + factor * 7]

        #if king
        if piece==5:
            if player==20:
                if position-1>=0 and position%8!=0:
                    if board[position-1]<20 and board[position-1]>=0:
                        list1=list1+[position-1]
                if position-9>=0 and position%8!=0:
                    if board[position - 9] < 20 and board[position - 9] >= 0:
                        list1 = list1 + [position - 9]
                if position-8>=0:
                    if board[position - 8] < 20 and board[position - 8] >= 0:
                        list1 = list1 + [position - 8]
                if position-7>=0 and (position-7)%8!=0:
                    if board[position - 7] < 20 and board[position - 7] >= 0:
                        list1 = list1 + [position - 7]
                if position+1<64 and (position+1)%8!=0:
                    if board[position+1]<20 and board[position+1]>=0:
                        list1=list1+[position+1]
                if position+9<64 and (position+9)%8!=0:
                    if board[position+9]<20 and board[position+9]>=0:
                        list1=list1+[position+9]
                if position + 8 < 64:
                    if board[position + 8] < 20 and board[position + 8] >= 0:
                        list1 = list1 + [position + 8]
                if position + 7 < 64 and position%8!=0:
                    if board[position + 7] < 20 and board[position + 7] >= 0:
                        list1 = list1 + [position + 7]

            if player==10:
                if position-1>=0 and position%8!=0:
                    if board[position-1]>=20:
                        list1=list1+[position-1]
                if position-9>=0 and position%8!=0:
                    if board[position - 9] >= 20:
                        list1 = list1 + [position - 9]
                if position-8>=0:
                    if board[position - 8] >= 20:
                        list1 = list1 + [position - 8]
                if position-7>=0 and (position-7)%8!=0:
                    if board[position - 7] >= 20 :
                        list1 = list1 + [position - 7]
                if position+1<64 and (position+1)%8!=0:
                    if board[position+1]>=20:
                        list1=list1+[position+1]
                if position+9<64 and (position+9)%8!=0:
                    if board[position+9]>=20 :
                        list1=list1+[position+9]
                if position + 8 < 64:
                    if board[position + 8] >= 20 :
                        list1 = list1 + [position + 8]
                if position + 7 < 64 and position%8!=0:
                    if board[position + 7] >= 20 :
                        list1 = list1 + [position + 7]
        if piece==1:
            if board[position] != 11 and board[position] != 21:
                return -1
            list1 = []
            # corners
            if position == 0:
                for i in [10, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 7:
                for i in [6, 15]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 56:
                for i in [-6, -15]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 63:
                for i in [-10, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # one in from corners (up/down direction)
            elif position == 8:
                for i in [10, 17, -6]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 15:
                for i in [6, 15, -10]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 48:
                for i in [-6, -15, 10]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 55:
                for i in [-10, -17, 6]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # one in from corners (right/left direction)
            elif position == 1:
                for i in [10, 17, 15]:
                    if not (19 - player) < board[position + i] < (26 - player):
                        list1 = list1 + [position + i]
            elif position == 6:
                for i in [6, 15, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 57:
                for i in [-6, -15, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 62:
                for i in [-10, -17, -15]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # one in from corners (diaganol direction)
            elif position == 9:
                for i in [10, 17, -6, 15]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 14:
                for i in [6, 15, -10, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 49:
                for i in [-6, -15, 10, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            elif position == 54:
                for i in [-10, -17, 6, -15]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle top row
            elif 1 < position < 6:
                for i in [6, 10, 15, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle left row
            elif 15 < position < 41 and position % 8 == 0:
                for i in [-6, 10, -15, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle right column
            elif 22 < position < 48 and position % 8 == 7:
                for i in [6, -10, 15, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle bottom row
            elif 57 < position < 62:
                for i in [-6, -10, -15, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle second row
            elif 9 < position < 14:
                for i in [-10, -6, 6, 10, 15, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle second column row
            elif 15 < position < 42 and position % 8 == 1:
                for i in [-17, 15, -6, 10, -15, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle seventh column
            elif 21 < position < 48 and position % 8 == 6:
                for i in [-15, -17, 6, -10, 15, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # 4 middle seventh row
            elif 49 < position < 54:
                for i in [6, 10, -6, -10, -15, -17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
            # middle 16 squares
            else:
                for i in [-6, 6, -10, 10, -15, 15, -17, 17]:
                    if not (-1 + player) < board[position + i] < (6 + player):
                        list1 = list1 + [position + i]
        
        cnt=0
        for i in list1:
            new=[]
            new=new+[position]
            new=new+[list1[cnt]]
            list1[cnt]=new
            cnt=cnt+1
        return list1

    def horizlist1(self,pos,player):
        list1=[]
        i=0
        index=pos-1
        conti=0
        if player==20:
            opponent=10
        if player==10:
            opponent=20
        metpiece=False
        while (conti==0 and metpiece==False):
            if ((index+1)%8)==0 or index-1<0:
                conti=1
                continue
            if ((index+1)%8)!=0 and index>=0 and index<64 :
                if self.pieces[index]>=player and self.pieces[index]<player+8:
                    metpiece=True
                    continue
                if self.pieces[index]!=0:
                    metpiece=True
                list1=list1+[index]
                if self.pieces[index]>=opponent and self.pieces[index]<opponent+8:
                    metpiece=True
                    continue
            if ((index+1)%8)==0 or index<0:
                conti=1
            index = index - 1
        index1=pos+1
        conti1=0
        metpiece1=False
        while (conti1==0 and metpiece1==False):
            if (index1%8==0 or index1>63):
                conti1=1
                continue
            if ((index1%8)!=0 and index1<64 and index1>=0):
                if self.pieces[index1]>=player and self.pieces[index1]<player+8:
                    metpiece1=True
                    continue
                list1=list1+[index1]
                if self.pieces[index1]>=opponent and self.pieces[index1]<opponent+8:
                    metpiece1=True
                    continue
                if self.pieces[index1]!=0:
                    metpiece1=True
            if (index1%8==0 or index1>63):
                conti1=1
            index1 = index1 + 1
        if list1==[]:
            return [False]
        return list1

    def diaglist1(self,pos,player):
        list1=[]
        index=pos-9
        conti=0
        metpiece=False
        if player==20:
            opponent=10
        if player==10:
            opponent=20
        #one way diagonal
        while (conti==0 and metpiece==False and index>=0):
            if index>=0 and (index+9)%8!=0:
                if self.pieces[index]>=player and self.pieces[index]<player+8:
                    metpiece=True
                    continue
                list1=list1+[index]
                if self.pieces[index]>=opponent and self.pieces[index]<opponent+8:
                    metpiece=True
                    continue
                if self.pieces[index]!=0:
                    metpiece=True
            if (index+9)%8==0 or index<0:
                conti=1
            index = index - 9

        index1=pos+9
        conti1=0
        metpiece1=False
        while (conti1==0 and metpiece1==False and index1<64):
            if (index1-8)%8!=0 and index<64:
                if self.pieces[index1]>=player and self.pieces[index1]<player+8:
                    metpiece1=True
                    continue
                list1=list1+[index1]
                if self.pieces[index1]>=opponent and self.pieces[index1]<opponent+8:
                    metpiece1=True
                    continue
                if self.pieces[index1]!=0:
                    metpiece1=True
            if (index1-8)%8==0 or index1>63:
                conti1=1
            index1 = index1 + 9

        #The other way diagonal
        index2=pos+7
        conti2=0
        metpiece2=False
        while (conti2==0 and metpiece2==False and index2<64):
            if (index2+1)%8!=0 and index2<64:
                if self.pieces[index2]>=player and self.pieces[index2]<player+8:
                    metpiece2=True
                    continue
                list1=list1+[index2]
                if self.pieces[index2]>=opponent and self.pieces[index2]<opponent+8:
                    metpiece2=True
                    continue
                if self.pieces[index2]!=0:
                    metpiece2=True
            if (index2+1)%8==0 or index2>63:
                conti2=1
            index2 = index2 + 7
        index3=pos-7
        conti3=0
        metpiece3=False
        while (conti3==0 and metpiece3==False and index3>=0):
            if index3%8!=0 and index3>=0:
                if self.pieces[index3]>=player and self.pieces[index3]<player+8:
                    metpiece3=True
                    continue
                list1=list1+[index3]
                if self.pieces[index3]>=opponent and self.pieces[index3]<opponent+8:
                    metpiece3=True
                    continue
                if self.pieces[index3]!=0:
                    metpiece3=True
            if index3%8==0 or index3<0:
                conti3=1
            index3 = index3 - 7

        if list1==[]:
            return [False]
        return list1

    def verticallist1(self, pos, player):
        list1=[]
        index=pos-8
        conti=0
        metpiece=False
        if player==20:
            opponent=10
        if player==10:
            opponent=20
        while (conti==0 and metpiece==False):
            if index>=0:
                if self.pieces[index]>=player and self.pieces[index]<player+8:
                    metpiece=True
                    break
                list1=list1+[index]
                if self.pieces[index]>=opponent and self.pieces[index]<opponent+8:
                    metpiece=True
                    break
                if self.pieces[index]!=0:
                    metpiece=True
            if index<0:
                conti=1
            index = index - 8
        index1=pos+8
        conti1=0
        metpiece1=False
        while (conti1==0 and metpiece1==False):
            if index1<64:
                if self.pieces[index1]>=player and self.pieces[index1]<player+8:
                    metpiece1=True
                    break
                list1=list1+[index1]
                if self.pieces[index1]>=opponent and self.pieces[index1]<opponent+8:
                    metpiece1=True
                    break
                if self.pieces[index1]!=0:
                    metpiece1=True
            if index1>63:
                conti1=1
            index1 = index1 + 8
        if list1==[]:
            return [False]
        return list1

    def IsPositionUnderThreat(self, board1, position, player):
        board=[]
        board=board+board1
        if (player == 10):
            if (board[position + 9] == 20 or board[position + 7] == 20):
                return True
            opp = self.GetPlayerPositions(board, 20)
            for i in opp:
                if (i == 10):
                    continue
                else:
                    moves = self.GetPieceLegalMoves(board, i)
                    for f in moves:
                        if f[1] == position:
                            return True
        if (player == 20):
            if (board[position - 9] == 10 or board[position - 7] == 10):
                return True
        opp = self.GetPlayerPositions(board, 10)
        for i in opp:
            if (i == 10):
                continue
            else:
                moves = self.GetPieceLegalMoves(board, i)
                for f in moves:
                    if (f == position):
                        return True
                    else:
                        return False

    def isWinner(self, board1, kingpos, player):
        board=[]
        board=board+board1
        spaces = [kingpos]
        if kingpos % 8 != 0:
            spaces += [kingpos - 9, kingpos + 7, kingpos - 1]
        if kingpos % 8 != 7:
            spaces += [kingpos + 9, kingpos - 7, kingpos + 1]
        if kingpos + 8 < 63:
            spaces += [kingpos + 8]
        if kingpos - 8 > 0:
            spaces += [kingpos - 8]
        for i in spaces:
            check = self.IsPositionUnderThreat(board, i, player)
            if check == False:
                return False

    def makeMove(self,moves, board1):
        if moves[1]==False:
            return board1
        board=[]
        board=board+board1
        board[moves[1]]=board[moves[0]]
        board[moves[0]]=0
        return board

    def genRandMove(self,player,board1):
        board=[]
        board=board+board1
        spots=self.GetPlayerPositions(board,player)
        random.shuffle(spots)
        done=False
        for i in spots:
            moves=self.GetPieceLegalMoves(board,i)
            random.shuffle(moves)
            for j in moves:
                if j[1]!=False:
                    move=j
                    done=True
                    break
            if done==True:
                break
        return move

    def chessPlayer(self, board, player):
        moves = [self.minimaxRoot(3, board, player)]
        for i in moves[1]:
            evalTree = heap()
            evalTree.add(i)
        return [True, moves[0], moves[1], evalTree]

    def minimaxRoot(self,depth, board1, player):
        board=board1
        bestMove = -10000
        if player == 10:
            pieces = self.GetPlayerPositions(board, 10)
            opponent = 20
        else:
            pieces = self.GetPlayerPositions(board, 20)
            opponent = 10
        moves = []
        for i in pieces:
            moves = moves + self.GetPieceLegalMoves(board, i)
        bestMoveFound=[False,False]
        count=0
        for i in range(0, len(moves), 1):
            copy = board
            tstmove = moves[i]
            boardcopy=self.makeMove(tstmove,board)
            if boardcopy==copy:
                count=count+1
                continue
            value = self.minimax_opponent(depth - 1, boardcopy, -10000, 10000, opponent)
            if value > bestMove:
                bestMove = value
                bestMoveFound = tstmove
        #if count==len(moves):
            #bestMoveFound=self.genRandMove(player,board)
        return bestMoveFound

    def minimax_opponent(self, depth, board1, alpha, beta, opponent):
        board=[]
        board=board+board1
        if depth == 0:
            return self.evaluateBoard(board, opponent)

        if opponent == 10:
            pieces = self.GetPlayerPositions(board, 10)
            player = 20
        else:
            pieces = self.GetPlayerPositions(board, 20)
            player = 10
        moves = []
        for i in pieces:
            moves =moves+ self.GetPieceLegalMoves(board, i)
        copy = board
        bestMove = -9999
        count=0
        for i in range(0, len(moves), 1):
            boardcopy=self.makeMove(moves[i],board)
            if boardcopy==copy:
                count=count+1
                continue
            bestMove = max(bestMove, self.minimax_player(depth - 1, boardcopy, alpha, beta, player))
            alpha = max(alpha, bestMove)
            if beta <= alpha:
                return bestMove
        #if count==len(moves):
            #bestMove=self.genRandMove(player,board)
        return bestMove

    def minimax_player(self, depth, board1, alpha, beta, player):
        # POSITION CNT?
        board=[]
        board=board+ board1
        if depth == 0:
            return self.evaluateBoard(board, player)

        if player == 10:
            pieces = self.GetPlayerPositions(board, 10)
            opponent = 20
        else:
            pieces = self.GetPlayerPositions(board, 20)
            opponent = 10
        moves = []
        for i in pieces:
            moves =moves+ self.GetPieceLegalMoves(board, i)
        copy = board
        bestMove = 9999
        count=0
        for i in range(0, len(moves), 1):
            boardcopy=self.makeMove(moves[i],board)
            if boardcopy==copy:
                count=count+1
                continue
            bestMove = min(bestMove, (self.minimax_opponent(depth - 1, boardcopy, alpha, beta, opponent)))
            beta = min(beta, bestMove)
            if beta <= alpha:
                return bestMove
        #if count==len(moves):
            #bestMove=self.genRandMove(player,board)
        return bestMove

    def evaluateBoard(self, board, player):
        totalEval = 0
        if player == 10:
            opponent = 20
        else:
            opponent = 10
        pieces = self.GetPlayerPositions(board, player)
        for i in pieces:
            totalEval = totalEval + self.GetPieceValue(board, i)
        pieces = self.GetPlayerPositions(board, opponent)
        for i in pieces:
            totalEval = totalEval - self.GetPieceValue(board, i)
        return totalEval

    def GetPieceValue(self, board, index):
        piece = board[index]
        if piece % 10 == 0:
            value = 10
        if piece % 10 == 1:
            value = 30
        if piece % 10 == 2:
            value = 30
        if piece % 10 == 3:
            value = 50
        if piece % 10 == 4:
            value = 90
        if piece % 10 == 5:
            value = 7000

        bking = [-3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4,-4, -5, -5, -4, -4, -3,
                 -2, -3, -3, -4, -4, -3, -3, -2,
                 -1, -2, -2, -2, -2, -2, -2, -1,
                 2, 2, 0, 0, 0, 0, 2, 2,
                 2, 3, 1, 0, 0, 1, 3, 2]
        wking = bking[::-1]
        queen = [-2, -1, -1, -.5, -.5, -1, -1, -2,
                 -1, 0, 0, 0, 0, 0, 0, -1,
                 -1, 0, .5, .5, .5, .5, 0, -1,
                 -.5, 0, .5, .5, .5, .5, 0, -.5,
                 -.5, 0, .5, .5, .5, .5, 0, -.5,
                 -1, 0, .5, .5, .5, .5, 0, -1,
                 -1, 0, 0, 0, 0, 0, 0, -1,
                 -2, -1, -1, -.5, -.5, -1, -1, -2]
        brook = [0, 0, 0, 0, 0, 0, 0, 0,
                 .5, 1, 1, 1, 1, 1, 1, .5,
                 -.5, 0, 0, 0, 0, 0, 0, .5,
                 -.5, 0, 0, 0, 0, 0, 0, -5,
                 -.5, 0, 0, 0, 0, 0, 0, -5,
                 -.5, 0, 0, 0, 0, 0, 0, -5,
                 -.5, 0, 0, 0, 0, 0, 0, -5,
                 -.5, 0, 0, 0, 0, 0, 0,
                 -5, 0, 0, 0, .5, .5, 0, 0, 0]
        wrook = brook[::-1]
        bknight = [-5, -4, -3, -3, -3, -3, -4, -5,
                   -4, -2, 0, 0, 0, 0, -2, -4,
                   -3, 0, 1, 1.5, 1.5, 1, 0, -3,
                   -3, .5, 1.5, 2, 2, 1.5, 1.5, -3,
                   -3, 0, 1, 1.5, 1.5, 1, 0, -3,
                   -3, .5, 1.5, 2, 2, 1.5, 1.5, -3,
                   -4, -2, 0, .5, .5, 0, -2, -4,
                   -5, -4, -3, -3, -3, -3, -4, -5]
        wknight = bknight[::-1]
        bbishop = [-2, -1, -1, -1, -1, -1, -1, -2,
                   -1, 0, 0, 0, 0, 0, 0, -1,
                   -1, 0, .5, 1, 1, .5, 0, -1,
                   -1, .5, .5, 1, 1, .5, .5, -1,
                   -1, 0, 1, 1, 1, 1, 0, -1,
                   -1, 1, 1, 1, 1, 1, -1, -1,
                   .5, 0, 0, 0, 0, 0,  .5,
                    -1, -2, -1, -1, -1, -1, -2,-1]
        wbishop = bbishop[::-1]
        bpawn = [7, 7, 7, 7, 7, 7, 7, 7,
                 5, 5, 5, 5, 5, 5, 5, 5,
                 1, 1, 2, 3, 3, 2, 1, 1,
                 .5, .5, 1, 2.5, 2.5, 1, .5, .5,
                 0, 0, 0, 2, 2, 0, 0, 0,
                 .5, -.5, -1, 0, 0, -1, -.5, .5,
                 .5, 1, 1, -2, -2, 1, 1, .5,
                 0, 0, 0, 0, 0, 0, 0, 0]
        wpawn = bpawn[::-1]
        if piece == 10:
            return value + wpawn[index]
        if piece == 11:
            return value + wknight[index]
        if piece == 12:
            return value + wbishop[index]
        if piece == 13:
            return value + wrook[index]
        if piece == 14:
            return value + queen[index]
        if piece == 15:
            return 50 + value + wking[index]
        if piece == 20:
            return value + bpawn[index]
        if piece == 21:
            return value + bknight[index]
        if piece == 22:
            return value + bbishop[index]
        if piece == 23:
            return value + brook[index]
        if piece == 24:
            return value + queen[index]
        if piece == 25:
            return 100 + value + bking[index]
        else:
            return False

    def chessPlayer(self, board, player):
        move = self.minimaxRoot(4,board,player)
        status = True
        return [status, move]

x=chess()
x.genEmptyBoard()
x.makeUserBoard()
print("This is EZ-chess. EZ-Chess is a primitive form of chess without the modern innovations of (a) castling, (b) pawns that move two spaces, and (c) en passant.")

done=False
while done==False:
    print("-----------WHITE-----------")
    x.makeUserBoard()
    x.printBoard()
    valid=False
    while valid==False:
        ans=input("Which piece would you like to move white?")
        cur=int(ans)
        next=int(input("Which place would you like to move to?"))
        moves=x.GetPieceLegalMoves(x.pieces, cur)
        for i in moves:
            if i[1]==next:
                valid=True
                x.pieces=x.makeMove(i,x.pieces)
                continue
        if valid==True:
            continue
        print("Sorry that is not a valid move set. Please try again")
    print("------BLACK IS THINKING------")
    x.makeUserBoard()
    x.printBoard()
    y=x.chessPlayer(x.pieces,20)
    x.pieces=x.makeMove([y[1][0],y[1][1]],x.pieces)
