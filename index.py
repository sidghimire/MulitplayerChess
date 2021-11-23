from os import kill
import pygame,sys
pygame.init()
size=width,height=640,640
brown=(185,134,103)
skin=(246,222,192)
green=(48,199,48)
black=(0,0,0)
lightGreen1=(139,231,139)
lightGreen2=(100,237,48)
red=(188,23,7)
grey=(255,255,255)
turn=1
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
    -3:"./Pieces/Chess_ndt60.png",
    -4:"./Pieces/Chess_bdt60.png",
    -5:"./Pieces/Chess_qdt60.png",
    -6:"./Pieces/Chess_kdt60.png",
}









#DONOT TOUCH CODES


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

def movePieces(box_number):
    global colored_y,colored_x,selected,selectedPiece,turn
    if(allowedMove(box_number)):
        if(board[box_number[1]][box_number[0]]==0 and (board[selectedPiece[1]][selectedPiece[0]]==1 or board[selectedPiece[1]][selectedPiece[0]]==-1)):
            board[box_number[1]][box_number[0]]=board[selectedPiece[1]][selectedPiece[0]]
            board[selectedPiece[1]][selectedPiece[0]]=0
            turn=turn*-1
        else:
            if( not (board[box_number[1]][box_number[0]]<0 and board[selectedPiece[1]][selectedPiece[0]]<0) or (board[box_number[1]][box_number[0]]>0 and board[selectedPiece[1]][selectedPiece[0]]>0)):
                board[box_number[1]][box_number[0]]=board[selectedPiece[1]][selectedPiece[0]]
                board[selectedPiece[1]][selectedPiece[0]]=0
                turn=turn*-1
        

    colored_x=None
    colored_y=None  
    selected=False
    selectedPiece=None
#DONOT TOUCH CODES
























#Logic For Pieces

def pawnLogic(i,j,get):
    global selected,selectedPiece
    guess=()
    killOptions=()
    
    if(j==6 and board[j][i]==-1):
        a=i*80
        b=j*80
        pos1=getBoxNumber(a+10,b-70)
        options=((i,j-1),(i,j-2))
        killList=((i+1,j-1),(i-1,j-1))
        selected=True
        selectedPiece=(pos1[1],pos1[0])
        for color in range(2):
            if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                if(board[options[color][1]][options[color][0]]==0):
                    if(get=="color"):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    guess=list(guess)
                    guess.append((options[color][0],options[color][1]))
                    guess=tuple(guess)
                selected=True
                selectedPiece=(i,j)

        for color in range(2):
            if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                if(board[killList[color][1]][killList[color][0]]>0):
                    if(get=="color"):
                        pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((killList[color][0],killList[color][1]))
                    killOptions=tuple(killOptions)
                selected=True
                selectedPiece=(i,j)
    else:
        a=i*80
        b=j*80
        pos1=getBoxNumber(a+10,b-70)
        options=(i,j-1)
        killList=((i+1,j-1),(i-1,j-1))

        selected=True
        selectedPiece=(i,j)
        if(options[1]<=7 and options[1]>=0 and options[0]<=7 and options[0]>=0):
            if(board[options[1]][options[0]]==0):
                if(get=="color"):
                    pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[0]*80,options[1]*80,80,80))
                guess=list(guess)
                guess.append((options[0],options[1]))
                guess=tuple(guess)
            selected=True
            selectedPiece=(i,j)
        for color in range(2):
            if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                if(board[killList[color][1]][killList[color][0]]>0):
                    if(get=="color"):
                        pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((killList[color][0],killList[color][1]))
                    killOptions=tuple(killOptions)
                selected=True
                selectedPiece=(i,j)





    if(j==1 and board[j][i]==1):
        a=i*80
        b=j*80
        pos1=getBoxNumber(a+10,b-70)
        options=((i,j+1),(i,j+2))
        killList=((i+1,j+1),(i-1,j+1))

        selected=True
        selectedPiece=(pos1[1],pos1[0])
        for color in range(2):
            if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                if(board[options[color][1]][options[color][0]]==0):
                    if(get=="color"):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    guess=list(guess)
                    guess.append((options[color][0],options[color][1]))
                    guess=tuple(guess)
                selected=True
                selectedPiece=(i,j)

        for color in range(2):
            if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                if(board[killList[color][1]][killList[color][0]]<0):
                    if(get=="color"):
                        pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((killList[color][0],killList[color][1]))
                    killOptions=tuple(killOptions)
                selected=True
                selectedPiece=(i,j)
    else:
        a=i*80
        b=j*80
        pos1=getBoxNumber(a+10,b-70)
        options=(i,j+1)
        killList=((i+1,j+1),(i-1,j+1))
        selected=True
        selectedPiece=(i,j)
        if(options[1]<=7 and options[1]>=0 and options[0]<=7 and options[0]>=0):
            if(board[options[1]][options[0]]==0):
                if(get=="color"):
                    pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[0]*80,options[1]*80,80,80))
                guess=list(guess)
                guess.append((options[0],options[1]))
                guess=tuple(guess)
            selected=True
            selectedPiece=(i,j)
        for color in range(2):
            if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                if(board[killList[color][1]][killList[color][0]]<0):
                    if(get=="color"):
                        pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((killList[color][0],killList[color][1]))
                    killOptions=tuple(killOptions)
                selected=True
                selectedPiece=(i,j)
    return ((guess,killOptions)) 
       

def hattiLogic(i,j,demand):
    options=()
    killOptions=()
    p=i+1
    #Right
    while(True):
        if(p<=7 and p>=0):
            if(board[j][p]==0):
                options=list(options)
                options.append((p,j))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[j][p]>0) or (board[j][i]>0 and board[j][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,j*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,j))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
    #Left
    p=i-1
    while(True):
        if(p<=7 and p>=0):
            if(board[j][p]==0):
                options=list(options)
                options.append((p,j))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[j][p]>0) or (board[j][i]>0 and board[j][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,j*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,j))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        #Top
    p=j-1
    while(True):
        if(p<=7 and p>=0):
            if(board[p][i]==0):
                
                options=list(options)
                options.append((i,p))
                options=tuple(options)
            else:
                if((board[j][i]<0 and board[p][i]>0) or (board[j][i]>0 and board[p][i]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(i*80,p*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((i,p))
                    killOptions=tuple(killOptions)
                break
        else:
            break
        p=p-1
    #bottom
    p=j+1
    while(True):
        if(p<=7 and p>=0):
            if(board[p][i]==0):
                options=list(options)
                options.append((i,p))
                options=tuple(options)
            else:
                if((board[j][i]<0 and board[p][i]>0) or (board[j][i]>0 and board[p][i]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(i*80,p*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((i,p))
                    killOptions=tuple(killOptions)
                break
        else:
            break
        p=p+1
    
    if(demand=="color"):return ((options,killOptions))





def uttaLogic(i,j,demand):
    options=()
    killOptions=()
    p=i+1
    q=j-1
    #Right top
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
        q=q-1

    
    #left top
    p=i-1
    q=j-1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        q=q-1
    
    

    #left bottom
    p=i-1
    q=j+1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        q=q+1


     #right bottom
    p=i+1
    q=j+1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
        q=q+1
    if(demand=="color"):return ((options,killOptions))


def mantriLogic(i,j,demand):
    options=()
    killOptions=()
    options=()
    killOptions=()
    p=i+1
    #Right
    while(True):
        if(p<=7 and p>=0):
            if(board[j][p]==0):
                options=list(options)
                options.append((p,j))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[j][p]>0) or (board[j][i]>0 and board[j][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,j*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,j*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,j))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
    #Left
    p=i-1
    while(True):
        if(p<=7 and p>=0):
            if(board[j][p]==0):
                options=list(options)
                options.append((p,j))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[j][p]>0) or (board[j][i]>0 and board[j][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,j*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,j*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,j))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        #Top
    p=j-1
    while(True):
        if(p<=7 and p>=0):
            if(board[p][i]==0):
                
                options=list(options)
                options.append((i,p))
                options=tuple(options)
            else:
                if((board[j][i]<0 and board[p][i]>0) or (board[j][i]>0 and board[p][i]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(i*80,p*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(i*80,p*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((i,p))
                    killOptions=tuple(killOptions)
                break
        else:
            break
        p=p-1
    #bottom
    p=j+1
    while(True):
        if(p<=7 and p>=0):
            if(board[p][i]==0):
                options=list(options)
                options.append((i,p))
                options=tuple(options)
            else:
                if((board[j][i]<0 and board[p][i]>0) or (board[j][i]>0 and board[p][i]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(i*80,p*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(i*80,p*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((i,p))
                    killOptions=tuple(killOptions)
                break
        else:
            break
        p=p+1
    


    p=i+1
    q=j-1
    #Right top
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,q*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
        q=q-1

    
    #left top
    p=i-1
    q=j-1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,q*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        q=q-1
    
    

    #left bottom
    p=i-1
    q=j+1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,q*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p-1
        q=q+1


     #right bottom
    p=i+1
    q=j+1
    while(True):
        if(p<=7 and p>=0 and q<=7 and q>=0):
            if(board[q][p]==0):
                options=list(options)
                options.append((p,q))
                options=tuple(options)
            else:                
                if((board[j][i]<0 and board[q][p]>0) or (board[j][i]>0 and board[q][p]<0)):
                    pygame.draw.rect(screen,red,pygame.Rect(p*80,q*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(p*80,q*80,80,80),width=1,border_radius=2)
                    killOptions=list(killOptions)
                    killOptions.append((p,q))
                    killOptions=tuple(killOptions)
                
                break
        else:
            break
        p=p+1
        q=q+1
    if(demand=="color"):return ((options,killOptions))


#Logic For Pieces





































#Show Movable Options


def show_movable_position(i,j):
    global selected,selectedPiece,turn
    pieceName=board[j][i]
    if((pieceName<0 and turn<0) or (pieceName>0 and turn>0)):

        if(pieceName==-1):
            if(j==6):
                a=i*80
                b=j*80
                pos1=getBoxNumber(a+10,b-70)
                options=((i,j-1),(i,j-2))
                killList=((i+1,j-1),(i-1,j-1))
                selected=True
                selectedPiece=(pos1[1],pos1[0])
                for color in range(2):
                    if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                        if(board[options[color][1]][options[color][0]]==0):
                            pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)

                for color in range(2):
                    if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                        if(board[killList[color][1]][killList[color][0]]>0):
                            pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)
            else:
                a=i*80
                b=j*80
                pos1=getBoxNumber(a+10,b-70)
                options=(i,j-1)
                killList=((i+1,j-1),(i-1,j-1))

                selected=True
                selectedPiece=(pos1[1],pos1[0])
                if(options[1]<=7 and options[1]>=0 and options[0]<=7 and options[0]>=0):
                    if(board[options[1]][options[0]]==0):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[0]*80,options[1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)
                for color in range(2):
                    if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                        if(board[killList[color][1]][killList[color][0]]>0):
                            pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)

       



        elif(pieceName==1):
            if(j==1):
                a=i*80
                b=j*80
                pos1=getBoxNumber(a+10,b-70)
                options=((i,j+1),(i,j+2))
                killList=((i+1,j+1),(i-1,j+1))
                selected=True
                selectedPiece=(pos1[1],pos1[0])
                for color in range(2):
                    if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                        if(board[options[color][1]][options[color][0]]==0):
                            pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)

                for color in range(2):
                    if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                        if(board[killList[color][1]][killList[color][0]]<0):
                            pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)
            else:
                a=i*80
                b=j*80
                pos1=getBoxNumber(a+10,b-70)
                options=(i,j+1)
                killList=((i+1,j+1),(i-1,j+1))

                selected=True
                selectedPiece=(pos1[1],pos1[0])
                if(options[1]<=7 and options[1]>=0 and options[0]<=7 and options[0]>=0):
                    if(board[options[1]][options[0]]==0):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[0]*80,options[1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)
                for color in range(2):
                    if(killList[color][1]<=7 and killList[color][1]>=0 and killList[color][0]<=7 and killList[color][0]>=0):
                        if(board[killList[color][1]][killList[color][0]]<0):
                            pygame.draw.rect(screen,red,pygame.Rect(killList[color][0]*80,killList[color][1]*80,80,80))
                        selected=True
                        selectedPiece=(i,j)






        elif(pieceName==-3 or pieceName==3):
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b-70)
            options=((i-1,j-2),(i-1,j+2),(i+1,j+2),(i+1,j-2),(i+2,j-1),(i+2,j+1),(i-2,j-1),(i-2,j+1))
            
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(8):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    if(board[options[color][1]][options[color][0]]==0):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    else:
                        if((board[options[color][1]][options[color][0]]<0 and board[j][i]>0) or (board[options[color][1]][options[color][0]]>0 and board[j][i]<0)):
                            pygame.draw.rect(screen,red,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)






        elif(pieceName==-2 or pieceName==2):
            options=hattiLogic(i,j,"color")
            options=options[0]
            pos1=(i,j)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(len(options)):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80),width=1,border_radius=2)

                    selected=True
                    selectedPiece=(i,j)







        elif(pieceName==-4 or pieceName==4):
            options=uttaLogic(i,j,"color")
            options=options[0]
            pos1=(i,j)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(len(options)):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)




        elif(pieceName==-5 or pieceName==5):
            options=mantriLogic(i,j,"color")
            options=options[0]
            pos1=(i,j)
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(len(options)):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    pygame.draw.rect(screen,grey,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80),width=1,border_radius=2)
                    selected=True
                    selectedPiece=(i,j)

        elif(pieceName==-6 or pieceName==6):
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b-70)
            options=((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1),(i-1,j-1))
            
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(8):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    if(board[options[color][1]][options[color][0]]==0):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                        pygame.draw.rect(screen,grey,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80),width=1,border_radius=2)

                    else:
                        if((board[options[color][1]][options[color][0]]<0 and board[j][i]>0) or (board[options[color][1]][options[color][0]]>0 and board[j][i]<0)):
                            pygame.draw.rect(screen,red,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)

        elif(pieceName==-3 or pieceName==3):
            a=i*80
            b=j*80
            pos1=getBoxNumber(a+10,b-70)
            options=((i-1,j-2),(i-1,j+2),(i+1,j+2),(i+1,j-2),(i+2,j-1),(i+2,j+1),(i-2,j-1),(i-2,j+1))
            
            selected=True
            selectedPiece=(pos1[1],pos1[0])
            for color in range(8):
                if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                    if(board[options[color][1]][options[color][0]]==0):
                        pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    else:
                        if((board[options[color][1]][options[color][0]]<0 and board[j][i]>0) or (board[options[color][1]][options[color][0]]>0 and board[j][i]<0)):
                            pygame.draw.rect(screen,red,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                    selected=True
                    selectedPiece=(i,j)
    #Show Movable Options





















#Check if Move is allowed


def allowedMove(boxNumber):
    global selectedPiece,selected
    pieceName=board[selectedPiece[1]][selectedPiece[0]]
    if(pieceName==-1):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=pawnLogic(i,j,"color")
        killList=options[1]
        options=options[0]
        options=list(options)
        for addKillList in range(len(killList)):
            options.append(killList[addKillList])
        options=tuple(options)
        if(boxNumber in options):
            return True
    elif(pieceName==1):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=pawnLogic(i,j,"color")
        killList=options[1]
        options=options[0]
        options=list(options)
        for addKillList in range(len(killList)):
            options.append(killList[addKillList])
        options=tuple(options)
        if(boxNumber in options):
            return True
    elif(pieceName==-3 or pieceName==3):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=()
        guess=((i-1,j-2),(i-1,j+2),(i+1,j+2),(i+1,j-2),(i+2,j-1),(i+2,j+1),(i-2,j-1),(i-2,j+1))
        for check in range(len(guess)):
            a,b=guess[check][0],guess[check][1]
            if(a>=0 and a<=7 and b>=0 and b<=7):
                if((board[b][a]<0 and board[j][i]>0) or (board[b][a]>0 and board[j][i]<0) or board[b][a]==0):
                    options=list(options)
                    options.append((a,b))
                    options=tuple(options)

        if(boxNumber in options):
            return True
    

    elif(pieceName==-6 or pieceName==6):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=()
        guess=((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1),(i-1,j-1))
        for check in range(len(guess)):
            a,b=guess[check][0],guess[check][1]
            if(a>=0 and a<=7 and b>=0 and b<=7):
                if((board[b][a]<0 and board[j][i]>0) or (board[b][a]>0 and board[j][i]<0) or board[b][a]==0):
                    options=list(options)
                    options.append((a,b))
                    options=tuple(options)

        if(boxNumber in options):
            return True


    elif(pieceName==-2 or pieceName==2):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=hattiLogic(i,j,"color")
        killList=options[1]
        options=options[0]
        pos1=(i,j)
        selected=True
        selectedPiece=(pos1[1],pos1[0])
        for color in range(len(options)):
            if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                selected=True
                selectedPiece=(i,j)
        options=list(options)
        for addKillList in range(len(killList)):
            options.append(killList[addKillList])
        options=tuple(options)
        if(boxNumber in options):
            return True

    elif(pieceName==-4 or pieceName==4):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=uttaLogic(i,j,"color")
        killList=options[1]
        options=options[0]
        pos1=(i,j)
        selected=True
        selectedPiece=(pos1[1],pos1[0])
        for color in range(len(options)):
            if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                selected=True
                selectedPiece=(i,j)
        options=list(options)
        for addKillList in range(len(killList)):
            options.append(killList[addKillList])
        options=tuple(options)
        if(boxNumber in options):
            return True

    elif(pieceName==-5 or pieceName==5):
        i=selectedPiece[0]
        j=selectedPiece[1]
        options=mantriLogic(i,j,"color")
        killList=options[1]
        options=options[0]
        pos1=(i,j)
        selected=True
        selectedPiece=(pos1[1],pos1[0])
        for color in range(len(options)):
            if(options[color][1]<=7 and options[color][1]>=0 and options[color][0]<=7 and options[color][0]>=0):
                pygame.draw.rect(screen,lightGreen1,pygame.Rect(options[color][0]*80,options[color][1]*80,80,80))
                selected=True
                selectedPiece=(i,j)
        options=list(options)
        for addKillList in range(len(killList)):
            options.append(killList[addKillList])
        options=tuple(options)
        if(boxNumber in options):
            return True

#Check if Move is allowed


### MINMAX Algorithm


def countNumOpp(board):
    count=0
    for i in range(8):
        for j in range(8):
            if(board[i][j]>0):
                count=count+1
    return count



    










#Main Part

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


#Main Part