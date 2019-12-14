import pygame
from tkinter import *

pygame.init()
pygame.font.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((1400, 1000))
def message_display(color,xy,message):
    used_font = None
    size = 34
    font_object = pygame.font.Font(used_font, size)
    rendered_text = font_object.render(message, True, (color))
    gameDisplay.blit(rendered_text,(xy))
    pygame.display.update()
def circ_disp(x,y,radius,colour):
    pygame.draw.circle(gameDisplay, colour, (x,y), radius,2)
    pygame.draw.circle(gameDisplay, colour, (x, y), 2, 2)
def run_gui ():
    root = Tk()
    root.geometry("500x250+900+300")
    root.resizable(False, False)
    Label(root, text='Enter radius of circle 1 : (px)', font=26).place(x=20,y=50)
    rad1 = Entry(root,width=10)
    rad1.place(x=260,y=50)
    Label(root, text='Enter radius of circle 2 : (px)', font=26).place(x=20, y=100)
    rad2 = Entry(root, width=10)
    rad2.place(x=260, y=100)
    Label(root, text='Enter distance between the 2 circles : (px)', font=26).place(x=20, y=150)
    dist = Entry(root, width=10)
    dist.place(x=370, y=150)
    u = Button(root, text="Submit", command=lambda: task(int(rad1.get()), int(rad2.get()), int(dist.get())))
    u.place(x=200, y=200)
    Label(root, text='note : all distances must be positive', font="Times_New_Roman 12 italic").place(x=20, y=5)
    root.mainloop()

def task(rad1,rad2,dist):
    gameDisplay.fill(black)
    circ_disp(700-(dist//2),500,rad1,red)
    circ_disp(700+(dist//2),500,rad2,blue)
    if int(rad1)<0 or int(rad2)<0 or int(dist)<0:
        gameDisplay.fill(black)
        message_display(green,(100,100),"please enter a positive distance value")
    elif rad2+rad1 == dist:
        message_display(green,(100,100),"The circles are tangential")
    elif abs(rad1-rad2) == dist:
        message_display(green, (100, 100), "The circles are tangential")
    elif dist == 0:
        message_display(green, (100, 100), "The circles are concentric")
    elif (rad2+rad1 < dist and dist!=0):
        message_display(green,(100,100),"The circles have no points of intersection")
    elif min(rad1,rad2)+dist<max(rad2,rad1):
        message_display(green, (100, 100), "The circles have no points of intersection")
    elif rad2+rad1 > dist and dist!=0:
        message_display(green,(100,100),"The circles have two points of intersection")


if __name__ == "__main__":
    run_gui()
