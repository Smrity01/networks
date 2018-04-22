from tkinter import *
import time

#.................................all 3 frame in a window are successfully sent...................................
#case 1
#when all frames and acknowledgement received sucessfully
def move_frame(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            canvas.update()
        time.sleep(0.25)
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
    #return

#...................................in a window size 2nd frame is lost.............................
#case 2
#when 2 frames may lost but acknowledgement received sucessfully of first frame
def lost_secondframe(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<22):
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
        if (i==25):
            canvas.delete(frame2)
            canvas.update()
        if (i==36 ):
            canvas.delete(frame3)
            canvas.update()
        if (i>65):
            timeout = canvas.create_text(450,250,text="oops...time out resend frame",font="Times 15 italic bold")
            canvas.update()
            time.sleep(2)
            canvas.delete(timeout)
#...................................in a window size 1st frame is lost so, all three frames lost.............................
#case 3
#when all 3 frames may lost 
def lost_allframe(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        if (i<20):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<31):
            canvas.move(frame2,30,0)
            canvas.update()
        if (i>10 and i<36):
            canvas.move(frame3,30,0)
            canvas.update()
        if (i==25):
            canvas.delete(frame1)
            canvas.update()
        if (i==31):
            canvas.delete(frame2)
            canvas.update()
        if (i==37 ):
            canvas.delete(frame3)
            canvas.update()
    timeout = canvas.create_text(450,250,text="Timeout..! As First frame is lost other were discarded",font="Times 15 italic bold")
    canvas.update()
    time.sleep(3)
    canvas.delete(timeout)

#.................................last(3rd) frame in a windoe is lost...................................
#case 4 
#when 3rd frame is lost and first 2 frame's acknowledgement received sucessfully
def last_frame(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            canvas.update()
        time.sleep(0.25)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<31):
            canvas.move(frame2,30,0)
            canvas.update()
        if (i>10 and i<28):
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
        if (i==33):
            canvas.delete(frame3)
            canvas.update()
    timeout = canvas.create_text(450,250,text="Timeout..! As last frame is lost, slide the window until this frame",font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(timeout)
#//////////////////////When ACKNOWLEDGEMENT of first frame is lost////////////////////////////////////////
#.....acknowledgement lost of first frame
def ack_lost(frame1,frame2,frame3,counter): # NOT COMPLETE
     for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            canvas.update()
        time.sleep(0.25)
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
            
    #return
#............................................................exceptional cases........................................
#.......................when less than windoe size frame are left at the end....................
#exceptional case
#to send 1 frames 
def sendone_frame(frame1Rframe1,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>26 and i<55):
            canvas.itemconfig(frame1, fill="green")
            canvas.itemconfig(Rframe1, fill="red")
            canvas.move(frame1,-27,0)
            canvas.update()
    #return
#exceptional case
#to send 2 frames
def sendtwo_frame(frame1,frame2,Rframe1,Rframe2,counter):
    for i in range(1,67):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        if (i<26):
            canvas.move(frame1,30,0)
            canvas.update()
        if (i>5 and i<31):
            canvas.move(frame2,30,0)
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
            
def draw_frame(x1,x2,index,color):
    return canvas.create_rectangle(x1,100+index,x2,150+index,fill=color)
def draw_canvas(counter):
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

    last_frame(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter)
    frame1 = draw_frame(50,120,0,'red')
    frame2 = draw_frame(50,120,54,'red')
    frame3 = draw_frame(50,120,109,'red')
    #when 2nd frame from 2nd window is lost
    '''
    time.sleep(1)
    move_frame(frame1,frame2,frame3,Rframe1,Rframe2,Rframe3,counter)
    time.sleep(1)
    lost_frame(frame4,frame5,frame6,Rframe4,Rframe5,Rframe6,counter)
    frame5 = draw_frame(50,120,225,'red')
    frame6 = draw_frame(50,120,280,'red')
    frame7 = draw_frame(50,120,340,'red')
    move_frame(frame5,frame6,frame7,Rframe5,Rframe6,Rframe7,counter)
    sendtwo_frame(frame8,frame9,Rframe8,Rframe9,counter)
    '''
    
root = Tk()
canvas = Canvas(root,width = 900,height = 900)
canvas.pack()
canvas.create_text(100,50,text="Sender",font="Times 20 italic bold")
canvas.create_text(800,50,text="Receiver",font="Times 20 italic bold")
counter = 0
timer = canvas.create_text(450, 650, text="00", font="Times 30 italic bold")
draw_canvas(counter)

root.mainloop()
