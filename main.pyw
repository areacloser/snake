from time import time
from tkinter import *
from random import randint

sttime = time()
lastsep = 0
snpos = [[1,0],[1,1],[1,2],[1,3]]
food = [randint(0,49), randint(0,49)]
way = 2
over = 0
score = 0

win = Tk()
win.resizable(0, 0)
win.geometry("+200+20")
win.title("贪吃蛇 V0.9.2 -- By lanlan2_        Score:%d" %score)
win.iconbitmap("icon.ico")
win.config(bg="aliceblue")

can = Canvas(win, height=500, width=500, borderwidth=0, relief=FLAT, bg="whitesmoke")
can.config(highlightthickness=0)
can.pack()

def drawb(x, y, tp):
    if tp == -1:
        tpa = "Red"
    elif tp == 0:
        tpa = "Whitesmoke"
    elif tp == 1:
        tpa = "Green"
    else:
        tpa = "Blue"
    can.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill=tpa, outline=tpa)

def draws():
    drawb(food[0], food[1], -1)
    for i in range(len(snpos)):
        if i+1 == len(snpos):
            drawb(snpos[i][0], snpos[i][1], 1)
        else:
            drawb(snpos[i][0], snpos[i][1], 2)
          
def moveup(event):
    global way, sttime, lastsep
    if (way == 3 or way == 4) and time()-sttime-lastsep > 0.1:
        way = 1
        lastsep = time()-sttime
    
def movedown(event):
    global way, sttime, lastsep
    if (way == 3 or way == 4) and time()-sttime-lastsep > 0.1:
        way = 2
        lastsep = time()-sttime
    
def moveleft(event):
    global way, sttime, lastsep
    if (way == 1 or way == 2) and time()-sttime-lastsep > 0.1:
        way = 3
        lastsep = time()-sttime
    
def moveright(event):
    global way, sttime, lastsep
    if (way == 1 or way == 2) and time()-sttime-lastsep > 0.1:
        way = 4
        lastsep = time()-sttime
        

def end():
    win.title("贪吃蛇 V0.9.2 -- By lanlan2_")
    can.create_text(250, 200, text="Game Over", fill="lightgrey", font="黑体 32 bold")
    can.create_text(250, 250, text="Score:%d" %score, fill="lightgrey", font="黑体 32 bold")
    
def update():
    global food, over, score
    can.delete("all")
    if over == 1:
        end()
        return
    snpos.pop(0)
    if [snpos[-1][0], snpos[-1][1]] == food:
        snpos.insert(0, [snpos[0][0], snpos[0][1]])
        food = [randint(0, 49), randint(0, 49)]
        score += 10
        win.title("贪吃蛇 V0.9.2 -- By lanlan2_        Score:%d" %score)
    if way == 1:
        if [snpos[-1][0], snpos[-1][1]-1] not in snpos and snpos[-1][0] >= 0 and snpos[-1][1]-1 >= 0 and snpos[-1][0] <= 49 and snpos[-1][1]-1 <= 49:
            snpos.append([snpos[-1][0], snpos[-1][1]-1])
            draws()
            win.update()
        else:
            over = 1
    elif way == 2:
        if [snpos[-1][0], snpos[-1][1]+1] not in snpos and snpos[-1][0] >= 0 and snpos[-1][1]+1 >= 0 and snpos[-1][0] <= 49 and snpos[-1][1]+1 <= 49:
            snpos.append([snpos[-1][0], snpos[-1][1]+1])
            draws()
            win.update()
        else:
            over = 1
    elif way == 3:
        if [snpos[-1][0]-1, snpos[-1][1]] not in snpos and snpos[-1][0]-1 >= 0 and snpos[-1][1] >= 0 and snpos[-1][0]-1 <= 49 and snpos[-1][1] <= 49:
            snpos.append([snpos[-1][0]-1, snpos[-1][1]])
            draws()
            win.update()
        else:
            over = 1
    elif way == 4:
        if [snpos[-1][0]+1, snpos[-1][1]] not in snpos and snpos[-1][0]+1 >= 0 and snpos[-1][1] >= 0 and snpos[-1][0]+1 <= 49 and snpos[-1][1] <= 49:
            snpos.append([snpos[-1][0]+1, snpos[-1][1]])
            draws()
            win.update()
        else:
            over = 1

def main():
    update()
    win.after(100, main)

main()
win.bind("<KeyPress-Up>", moveup)
win.bind("<KeyPress-Down>", movedown)
win.bind("<KeyPress-Left>", moveleft)
win.bind("<KeyPress-Right>", moveright)
win.mainloop()
