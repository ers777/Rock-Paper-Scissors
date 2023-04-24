from tkinter import *
from tkinter.ttk import *
import random
from playsound import playsound
from threading import Thread
import multiprocessing
from playsound import playsound
global r
r=[]
class GFG:
    def __init__(self, master=None,canvas=None):
        self.master = master
        self.canvas = canvas
        f=['red','black','green']
        self.color=random.choice(f)


        # to take care movement in x direction
        self.x = random.randrange(-5,5)
        # to take care movement in y direction
        self.y = random.randrange(-5,5)

        # canvas object to create shape
        self.v = Label(master, text='fgfgfggfgf')
        self.v.place(x=10, y=150)


        # creating rectangle
        self.rectangle = self.canvas.create_oval(
            5, 5, 25, 25, fill=self.color)
        self.canvas.move(self.rectangle,random.randrange(0,380),random.randrange(0,380))

        self.canvas.pack()

        # calling class's movement method to
        # move the rectangle
        self.movement()

    def movement(self):
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle, self.x, self.y)
        x0, y0, x1, y1= self.canvas.coords(self.rectangle)
        self.v['text']=str(x0)+' : '+str(y0)+"="+str(x0)+' : '+str(y0)
        if x0<=0 or x0>=400-20:
            self.x=self.x*-1;
        elif y0<=0 or y0>=400-20:self.y=self.y*-1

        color = self.canvas.itemcget(self.rectangle, "fill")
        r.append(color)
        b=self.color


        items = self.canvas.find_overlapping(x0, y0, x1, y1)
        for item in filter(lambda i: i is not self.rectangle, items):
            color1 = self.canvas.itemcget(item, "fill")
            # print(color,color1)


            if (color == 'red' and color1 == 'black')or(color == 'black' and color1 == 'red') :
                b='red'
            elif (color == 'black' and color1 == 'green') or (color == 'green' and color1 == 'black'):
                b='black'

            elif (color == 'green' and color1 == 'red')or (color == 'red' and color1 == 'green'):
                b='green'

            elif color==color1:
                b=color


            self.canvas.itemconfig(item, fill=b)
            self.x = self.x*-1+1;
            self.y = self.y*-1;
        objects = canvas.find_all()
        g=[]
        global t
        [g.append(canvas.itemcget(i, 'fill')) for i in objects]
        if len(set(g))==1:
            self.v['text']="win is "+g[0]
            self.x=0
            self.y=0

        g.clear()



        self.canvas.after(20, self.movement)
    # for motion in negative x direction
    def left(self, event):
        print(event.keysym)
        self.x = -5
        self.y = 0

    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        self.x = 5
        self.y = 0

    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5

    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5
    # def eyes(self,master=None,canvas=None):
    #     self.master = master
    #     self.canvas = canvas
    #     self.canvas1 = Canvas(self.canvas, width=500, height=500)
    #
    #     self.rectangle = self.canvas.create_oval(
    #         5, 5, 25, 25, fill='blue')
    #     self.canvas.move(self.rectangle,random.randrange(0,380),random.randrange(0,380))
    #
    #     self.canvas1.pack()
global f1
f1=[]
global t
t = Thread(target=lambda: playsound('Dark Souls 3 OST.mp3'), daemon=True)

if __name__ == "__main__":

    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()

    canvas = Canvas(master, width=400, height=400)

    master.resizable(0, 0)
    master.wm_attributes('-topmost', 1)
    for i in range(10):
        f1.append(GFG(master,canvas))
    # f1[0].eyes(master,canvas)


    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    master.bind("<KeyPress-Left>", lambda e: f1[0].left(e))
    master.bind("<KeyPress-Right>", lambda e: f1[0].right(e))
    master.bind("<KeyPress-Up>", lambda e: f1[0].up(e))
    master.bind("<KeyPress-Down>", lambda e: f1[0].down(e))

    t.start()

    # Infinite loop breaks only by interrupt
    mainloop()