from tkinter import *
import time
def draw_frame():
    frame = canvas.create_rectangle(50,100,120,150,fill='red')
    time.sleep(5)
    for i in range(1,25):
        time.sleep(0.5)
        canvas.move(frame,30,0)
        canvas.update()
    for i in range(1,25):
        time.sleep(0.5)
        canvas.move(frame,-10,0)
        canvas.update()
root = Tk()
canvas = Canvas(root,width = 900,height = 500)
canvas.pack()
canvas.create_text(100,50,text="Sender",font="Times 20 italic bold")
canvas.create_text(800,50,text="Receiver",font="Times 20 italic bold")
draw_frame()
root.mainloop()
