'''
Program         : Selective Repeat Protocol
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
    begins to work, the frames begin to send according to the Selective Repeat Algorithm
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
    lost = canvas.create_text(450,650,text="",font="Times 20 italic bold")
    
    # Runner Loop
    for i in range(1,340):
        time.sleep(0.15)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<26):
            canvas.move(frame2,30,0)
            canvas.update()
        if (i>26 and i<52):
            canvas.itemconfig(frame1, fill="green")
            canvas.itemconfig(Rframe1, fill="red")
            canvas.move(frame1,-30,0)
            canvas.update()
        if (i==55):
            timeout = canvas.create_text(450,650,text="Time out,frame lost",font="Times 20 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
            canvas.delete(frame2)
            canvas.itemconfig(Rframe2, fill="black")
            frame2 = draw_frame(50,120,54,'red')
        if (i>56 and i<82):
            canvas.move(frame2,30,0)
            canvas.update()
        if (i>60 and i<86):
            canvas.move(frame3,30,0)
            canvas.update()
        if (i>82 and i<108):
            canvas.itemconfig(frame2, fill="green")
            canvas.itemconfig(Rframe2, fill="red")
            canvas.move(frame2,-30,0)
            canvas.update()
        if (i>86 and i<112):
            canvas.itemconfig(frame3, fill="green")
            canvas.itemconfig(Rframe3, fill="red")
            canvas.move(frame3,-30,0)
            canvas.update()
        if(i>113 and i<139):
            canvas.move(frame4,30,0)
            canvas.update()
        if (i>118 and i<144):
            canvas.move(frame5,30,0)
            canvas.update()
        if (i>139 and i<140):
            canvas.itemconfig(frame4, fill="green")
            canvas.itemconfig(Rframe4, fill="red")
            canvas.move(frame4,-29,0)
            canvas.update()
        if (i>144 and i<170):
            canvas.itemconfig(frame5, fill="green")
            canvas.itemconfig(Rframe5, fill="red")
            canvas.move(frame5,-30,0)
            canvas.update()
        if (i==170):
            timeout = canvas.create_text(450,650,text="acknowledgement lost",font="Times 20 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
            canvas.delete(frame4)
            canvas.itemconfig(Rframe4, fill="black")
            frame4 = draw_frame(50,120,170,'red')
        if(i>171 and i<197):
            canvas.move(frame4,30,0)
            canvas.update()
        if (i>176 and i<202):
            canvas.move(frame6,30,0)
            canvas.update()
        if (i>197 and i<223):
            canvas.itemconfig(frame4, fill="green")
            canvas.itemconfig(Rframe4, fill="red")
            canvas.move(frame4,-30,0)
            canvas.update()
        if (i>202 and i<228):
            canvas.itemconfig(frame6, fill="green")
            canvas.itemconfig(Rframe6, fill="red")
            canvas.move(frame6,-30,0)
            canvas.update()
        if(i>228 and i<254):
            canvas.move(frame7,30,0)
            canvas.update()
        if (i>233 and i<259):
            canvas.move(frame8,30,0)
            canvas.update()
        if (i>254 and i<280):
            canvas.itemconfig(frame7, fill="green")
            canvas.itemconfig(Rframe7, fill="red")
            canvas.move(frame7,-30,0)
            canvas.update()
        if (i>259 and i<270):
            canvas.itemconfig(frame8, fill="green")
            canvas.itemconfig(Rframe8, fill="red")
            canvas.move(frame8,-30,0)
            canvas.update()
        if (i==281):
            timeout = canvas.create_text(450,650,text="acknowledgement lost",font="Times 20 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
            canvas.delete(frame8)
            canvas.itemconfig(Rframe8, fill="black")
            frame8 = draw_frame(50,120,395,'red')
        if(i>281 and i<307):
            canvas.move(frame8,30,0)
            canvas.update()
        if (i>286 and i<312):
            canvas.move(frame9,30,0)
            canvas.update()
        if (i>307 and i<333):
            canvas.itemconfig(frame8, fill="green")
            canvas.itemconfig(Rframe8, fill="red")
            canvas.move(frame8,-30,0)
            canvas.update()
        if (i>312 and i<338):
            canvas.itemconfig(frame9, fill="green")
            canvas.itemconfig(Rframe9, fill="red")
            canvas.move(frame9,-30,0)
            canvas.update()
        
# -----------------------------------------------------------------------------
# Main handler block
'''
Creating the canvas for the graphical user interface.

Module Used : Tkinter for GUI
'''
root = Tk()
root.title("Selective Repeat")
canvas = Canvas(root,width = 900,height = 900)
canvas.pack()
canvas.create_text(100,50,text="Sender",font="Times 20 italic bold")
canvas.create_text(800,50,text="Receiver",font="Times 20 italic bold")
#timer = canvas.create_text(450, 650, text="00", font="Times 30 italic bold")
draw_canvas()

root.mainloop()
# -----------------------------------------------------------------------------