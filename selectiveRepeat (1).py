from tkinter import *
import time

def draw_frame(index, color):
    return canvas.create_rectangle(50, 100 + index, 120, 150 + index, fill=color)

def move_frame(frame,index):
    for i in range(1, 26):
        time.sleep(0.25)
        if (i < 26):
            canvas.move(frame, 30, 0)
            canvas.update()


def move_ack(frame,index):
    for i in range(1,55):
        time.sleep(0.25)
        if (i > 0 and i < 29):
            canvas.itemconfig(frame, fill="green")
            canvas.move(frame, -27, 0)
            canvas.update()

def draw_window():
    frame1 = draw_frame(0, 'yellow')
    frame2 = draw_frame(54, 'yellow')
    frame3 = draw_frame(109, 'yellow')
    frame4 = draw_frame(170, 'blue')
    frame5 = draw_frame(225, 'blue')
    frame6 = draw_frame(280, 'blue')
    frame7 = draw_frame(340, 'red')
    frame8 = draw_frame(395, 'red')
    frame9 = draw_frame(450, 'red')

    allFrames = [frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9]

    '''
    for i in range(0,len(allFrames),3):
        move_frame(allFrames[i], i + 1)
        move_frame(allFrames[i+1], i + 2)
        move_frame(allFrames[i+2], i + 3)

        #move_ack(allFrames[i],i+1)
    '''
    move_frame(frame1, 1)
    move_frame(frame2, 2)
    canvas.delete(frame2)
    t1 = canvas.create_text(450, 250, text='Frame lost, resending again.', font='Times 15 italic bold')
    canvas.update()
    time.sleep(2)
    canvas.delete(t1)
    move_frame(frame3, 3)
    frame2 = draw_frame(54, 'yellow')
    move_frame(frame2,2)

root = Tk()
root.title('Selective Repeat')
canvas = Canvas(root, width=900, height=900)
canvas.pack()
canvas.create_text(100, 50, text="Sender", font="Times 20 italic bold")
canvas.create_text(800, 50, text="Receiver", font="Times 20 italic bold")
draw_window()
root.mainloop()