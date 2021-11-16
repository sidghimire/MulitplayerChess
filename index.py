#create window for pygame
import pygame,sys

#initialize pygame
pygame.init()
size=width,height=640,640
brown=(185,134,103)
skin=(246,222,192)
green=(48,199,48)
lightGreen1=(139,231,139)
lightGreen2=(100,237,48)
red=(188,23,7)
colored_x=None
colored_y=None
selected=False
selectedPiece=None

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Chess AI")

board=[[2,3,4,5,6,4,3,2],
        [1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [-1,-1,-1,-1,-1,-1,-1,-1],
        [-2,-3,-4,-5,-6,-4,-3,-2]]

assignPieces={
    0:"./Pieces/null.png",
    1:"./Pieces/Chess_plt60.png",
    2:"./Pieces/Chess_rlt60.png",
    3:"./Pieces/Chess_nlt60.png",
    4:"./Pieces/Chess_blt60.png",
    5:"./Pieces/Chess_qlt60.png",
    6:"./Pieces/Chess_klt60.png",
    -1:"./Pieces/Chess_pdt60.png",
    -2:"./Pieces/Chess_rdt60.png",
    -3:"./Pieces/Chess_bdt60.png",
    -4:"./Pieces/Chess_ndt60.png",
    -5:"./Pieces/Chess_qdt60.png",
    -6:"./Pieces/Chess_kdt60.png",
}




#Draw Board
def draw_board():
    color=1
    initY=0
    for x in range(8):
        initX=0
        for y in range(8):
            if color==1:
                pygame.draw.rect(screen,skin,pygame.Rect(initX,initY,80,80))
                color=color*(-1)

            else:
                pygame.draw.rect(screen,brown,pygame.Rect(initX,initY,80,80))
                color=color*(-1)
            initX=initX+80
        color=color*(-1)
        initY=initY+80

#Add Pieces

def draw_pieces():
    initY=10
    a=0
    for x in range(8):
        initX=10
        b=0
        for y in range(8):
            piece=pygame.image.load(assignPieces[board[a][b]])
            screen.blit(piece,(initX,initY))
            initX=initX+80
            b=b+1
        initY=initY+80
        a=a+1

def color_clicked_box(i,j):
    a=i*80
    b=j*80
    if(board[j][i]==0):
        pygame.draw.rect(screen,red,pygame.Rect(a,b,80,80))
    else:
        pygame.draw.rect(screen,green,pygame.Rect(a,b,80,80))
        show_movable_position(i,j)

def show_movable_position(i,j):
    global selected,selectedPiece
    pieceName=board[j][i]
    if(pieceName==-1):
        if(j==6):
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b-70)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            if(board[pos1[1]][pos1[0]]==0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(a,b-80,80,80))
                pos1=getBoxNumber(a+10,b-150)
                if(board[pos1[1]][pos1[0]]==0):
                    pygame.draw.rect(screen,lightGreen2,pygame.Rect(a,b-160,80,80))
                selected=True
                selectedPiece=(i,j)
        else:
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b-70)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            if(board[pos1[1]][pos1[0]]==0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(a,b-80,80,80))
                selected=True
                selectedPiece=(i,j)

    elif(pieceName==1):
        if(j==1):
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b+90)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            if(board[pos1[1]][pos1[0]]==0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(a,b+80,80,80))
                pos1=getBoxNumber(a+10,b+150)
                if(board[pos1[1]][pos1[0]]==0):
                    pygame.draw.rect(screen,lightGreen2,pygame.Rect(a,b+160,80,80))
                selected=True
                selectedPiece=(i,j)
        else:
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b+90)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            if(board[pos1[1]][pos1[0]]==0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(a,b+80,80,80))
                selected=True
                selectedPiece=(i,j)



def getBoxNumber(x,y):
    locationX=None
    locationY=None
    for i in range(8):
        if (x>((i)*80) and x<((i+1)*80)):
            locationX=i
    for j in range(8):
        if (y>((j)*80) and y<((j+1)*80)):
            locationY=j
    return((locationX,locationY))


def allowedMove(boxNumber):
    global selectedPiece
    movablePosition=None
    pieceName=board[selectedPiece[1]][selectedPiece[0]]
    if(pieceName==-1):
        if(selectedPiece[1]==6):
            options=((selectedPiece[0],selectedPiece[1]-1),(selectedPiece[0],selectedPiece[1]-2))
            if(boxNumber in options):
                return True
        else:
            options=((selectedPiece[0],selectedPiece[1]-1))
            if(boxNumber == options):
                return True
    elif(pieceName==1):
        if(selectedPiece[1]==1):
            options=((selectedPiece[0],selectedPiece[1]+1),(selectedPiece[0],selectedPiece[1]+2))
            if(boxNumber in options):
                return True
        else:
            options=((selectedPiece[0],selectedPiece[1]+1))
            if(boxNumber == options):
                return True

def movePieces(box_number):
    global colored_y,colored_x,selected,selectedPiece
    allowedMove(box_number)
    if(allowedMove(box_number)):
        if(board[box_number[1]][box_number[0]]==0):
            board[box_number[1]][box_number[0]]=board[selectedPiece[1]][selectedPiece[0]]
            board[selectedPiece[1]][selectedPiece[0]]=0
    colored_x=None
    colored_y=None  
    selected=False
    selectedPiece=None

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            box_number=getBoxNumber(pos[0],pos[1])
            if(selected==True):
                movePieces(box_number)
                colored_x=None
                colored_y=None  
                selected=False
                selectedPiece=None
            else:
                colored_x=box_number[0]
                colored_y=box_number[1]
    draw_board()
    if(colored_x!=None and colored_y!=None):
        color_clicked_box(colored_x,colored_y)
    draw_pieces()

    pygame.display.flip()
