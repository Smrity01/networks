'''
Program         : Go Back N Protocol
'''

# Importing necessary libraries
from tkinter import *
import time
            
# -----------------------------------------------------------------------------
# Functions Definitions
def draw_frame(x1,x2,index,color):
    '''
    Drawing a rectangular frame to show the data packet.

    Parameters
    ----------
    x1 : dtype - int, x1 coordinate.
    x2 : dtype - int, x2 coordinate.
    index : dtype - int, parameter for y coordinate.
    color : dtype - string, the color of the rectangle.
    

    Returns
    -------
    dtype - canvas object,a rectangle which is used to display the data packet.

    Description
    -----------
    draw_frame function description.

    Approach
    --------
    member function of canvas module is used to draw a rectangle.
    '''
    return canvas.create_rectangle(x1,100+index,x2,150+index,fill=color)


def draw_canvas():
    '''
    Drawing a canvas for the interface of Go Back N protocol.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Description
    -----------
    draw_canvas function description.

    Approach
    --------
    Firstly, we made the initial frames to be sent to the receiver side. The newly created
    frames are at sender side now, before the working of the protocol. Once the protocol
    begins to work, the frames begin to send according to the Go Back N Algorithm
    member function of canvas module is used to draw a rectangle.
    '''
    
    # Creating the frames.
    frame1 = draw_frame(50,120,0,'red')
    Rframe1 = draw_frame(795,865,0,'black')
    frame2 = draw_frame(50,120,54,'red')
    Rframe2 = draw_frame(795,865,54,'black')
    frame3 = draw_frame(50,120,109,'red')
    Rframe3 = draw_frame(795,865,109,'black')
    frame4 = draw_frame(50,120,170,'red')
    Rframe4 = draw_frame(795,865,170,'black')
    frame5 = draw_frame(50,120,225,'red')
    Rframe5 = draw_frame(795,865,225,'black')
    frame6 = draw_frame(50,120,280,'red')
    Rframe6 = draw_frame(795,865,280,'black')
    frame7 = draw_frame(50,120,340,'red')
    Rframe7 = draw_frame(795,865,340,'black')
    frame8 = draw_frame(50,120,395,'red')
    Rframe8 = draw_frame(795,865,395,'black')
    frame9 = draw_frame(50,120,450,'red')
    Rframe9 = draw_frame(795,865,450,'black')

    # Creating an object of create_text.
    lost = canvas.create_text(450,650,text="",font="Times 20 italic bold")
    
    # Runner loop.
    for i in range(1,270):
        time.sleep(0.15)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<31):
            canvas.move(frame2,30,0)
            canvas.update()
        if (i>10 and i<36):
            canvas.move(frame3,30,0)
            canvas.update()
        if (i>26 and i<55):
            canvas.itemconfig(frame1, fill="green")
            canvas.itemconfig(Rframe1, fill="red")
            canvas.move(frame1,-27,0)
            canvas.update()
        if (i>31 and i<60):
            canvas.itemconfig(frame2, fill="green")
            canvas.itemconfig(Rframe2, fill="red")
            canvas.move(frame2,-27,0)
            canvas.update()
        if (i>36 and i<65):
            canvas.itemconfig(frame3, fill="green")
            canvas.itemconfig(Rframe3, fill="red")
            canvas.move(frame3,-27,0)
            canvas.update()
        if(i>55 and i<81):
            canvas.move(frame4,30,0)
            canvas.update()
        if (i>60 and i<75):
            canvas.move(frame5,30,0)
            canvas.update()
        if (i==75):
            canvas.itemconfig(lost,text = "Frame lost. Further frames discarded by receiver.")
            canvas.update()
        if (i==130):
            canvas.delete(lost)
            canvas.update()
        if (i>65 and i<91):
            canvas.move(frame6,30,0)
            canvas.update()
        if (i>81 and i<110):
            canvas.itemconfig(frame4, fill="green")
            canvas.itemconfig(Rframe4, fill="red")
            canvas.move(frame4,-27,0)
            canvas.update()
        if (i>111 and i<133):
            canvas.move(frame7,30,0)
            canvas.update()
        if (i==133):
            timeout = canvas.create_text(450,650,text="Time out...",font="Times 20 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
            canvas.delete(frame7)
            canvas.itemconfig(Rframe7, fill="black")
            canvas.delete(frame5)
            canvas.itemconfig(Rframe5, fill="black")
            canvas.delete(frame6)
            canvas.itemconfig(Rframe6, fill="black")
            frame6 = draw_frame(50,120,280,'red')
            frame7 = draw_frame(50,120,340,'red')
            frame5 = draw_frame(50,120,225,'red')
            canvas.update()
        if (i>134 and i<160):
            canvas.move(frame5,30,0)
            canvas.update()
        if (i>139 and i<165):
            canvas.move(frame6,30,0)
            canvas.update()
        if (i>144 and i<170):
            canvas.move(frame7,30,0)
            canvas.update()
        if (i>160 and i<189):
            canvas.itemconfig(frame5, fill="green")
            canvas.itemconfig(Rframe5, fill="red")
            canvas.move(frame5,-27,0)
            canvas.update()
        if (i>165 and i<194):
            canvas.itemconfig(frame6, fill="green")
            canvas.itemconfig(Rframe6, fill="red")
            canvas.move(frame6,-27,0)
            canvas.update()
        if (i>170 and i<190):
            canvas.itemconfig(frame7, fill="green")
            canvas.itemconfig(Rframe7, fill="red")
            canvas.move(frame7,-27,0)
            canvas.update()
        if (i==190):
            canvas.itemconfig(lost,text = "Acknowldegement lost. Further frames discarded by receiver...")
            canvas.update()
        if (i==205):
            canvas.delete(lost)
            canvas.update()
        if (i>189 and i<200):
            canvas.move(frame8,30,0)
            canvas.update()
        if (i>194 and i<200):
            canvas.move(frame9,30,0)
            canvas.update()
        if (i==203):
            timeout = canvas.create_text(450,650,text="Time out...",font="Times 20 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
            canvas.delete(frame7)
            canvas.itemconfig(Rframe7, fill="black")
            canvas.delete(frame8)
            canvas.delete(frame9)
            frame7 = draw_frame(50,120,340,'red')
            frame8 = draw_frame(50,120,395,'red')
            frame9 = draw_frame(50,120,450,'red')
        if (i>204 and i<229):
            canvas.move(frame7,30,0)
            canvas.update()
        if (i>209 and i<234):
            canvas.move(frame8,30,0)
            canvas.update()
        if (i>214 and i<239):
            canvas.move(frame9,30,0)
            canvas.update()
        if (i>229 and i<257):
            canvas.itemconfig(frame7, fill="green")
            canvas.itemconfig(Rframe7, fill="red")
            canvas.move(frame7,-27,0)
            canvas.update()
        if (i>234 and i<262):
            canvas.itemconfig(frame8, fill="green")
            canvas.itemconfig(Rframe8, fill="red")
            canvas.move(frame8,-27,0)
            canvas.update()
        if (i>239 and i<267):
            canvas.itemconfig(frame9, fill="green")
            canvas.itemconfig(Rframe9, fill="red")
            canvas.move(frame9,-27,0)
            canvas.update()

# -----------------------------------------------------------------------------
# Main handler block
'''
Creating the canvas for the graphical user interface.

Module Used : Tkinter for GUI
'''
root = Tk()
root.title("Go Back N")
canvas = Canvas(root,width = 900,height = 900)
canvas.pack()
canvas.create_text(100,50,text="Sender",font="Times 20 italic bold")
canvas.create_text(800,50,text="Receiver",font="Times 20 italic bold")
#timer = canvas.create_text(450, 650, text="00", font="Times 30 italic bold")
draw_canvas()
root.mainloop()
# -----------------------------------------------------------------------------