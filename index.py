#create window for pygame
import pygame,sys

#initialize pygame
pygame.init()
size=width,height=720,720
black=(0,0,0)
white=(200,200,200)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Chess AI")

w_pawn=pygame.image.load("./Pieces/pawn.png")
w_pawn=pygame.transform.scale(w_pawn,(43,75))
def draw_board():
    color=1
    
    initY=0
    for x in range(8):
        initX=0
        for y in range(8):
            if color==1:
                pygame.draw.rect(screen,white,pygame.Rect(initX,initY,90,90))
                color=color*(-1)

            else:
                pygame.draw.rect(screen,black,pygame.Rect(initX,initY,90,90))
                color=color*(-1)
            initX=initX+90
        color=color*(-1)
        initY=initY+90



while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
    draw_board()
    screen.blit(w_pawn,(0,0))
    pygame.display.flip()
