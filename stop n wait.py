from tkinter import *
from random import *
import time
root = Tk()
canvas = Canvas(root,width = 900,height = 500)
canvas.pack()
canvas.create_text(100,50,text="Sender",font="Times 20 italic bold")
canvas.create_text(800,50,text="Receiver",font="Times 20 italic bold")

def sender_network():
    frame = input('enter data: ')
    return frame
    
def sender_physical(counter,timer):
    frame = draw_frame()
    #print('data received at physical layer of sender...')
    random = randint(1,4)
    print('sender random',random)
    if(random == 3):
        time.sleep(2)
        counter = frame_lost(frame,counter,timer)
        print('send same again')
        sender_physical(0,timer)
    else:
        move_frame(frame,counter,timer)
        receiver(frame,counter,timer)
        return counter

def receiver(frame,counter,timer):
    framerec = canvas.create_text(450,250,text="Frame is received",font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    #timeout = canvas.create_text(400,200,text="Time out",font="Times 20 italic bold")
    canvas.delete(framerec)
    canvas.delete(frame)
    #canvas.delete(timeout)
    print('data received at physical layer of receiver...')
    return 

def acknowledgement_lost(ack,counter,timer):
    for i in range(1,25):
        if(i%2 == 0):
            counter = counter+1
            canvas.delete(timer)
            timer = draw_timer(counter)
        time.sleep(0.25)
        canvas.move(ack,-10,0)
        canvas.update()
    acklost = canvas.create_text(450,250,text="ack lost",font="Times 15 italic bold")
    canvas.update()
    timeout = canvas.create_text(400,200,text="Time out",font="Times 20 italic bold")
    time.sleep(5)
    canvas.delete(acklost)
    canvas.delete(ack)
    canvas.delete(timeout)
    print('Acknowledgement lost')
    return

def acknowledgement_received(ack,counter,timer):
    move_ack(ack,counter,timer)
    ackrec = canvas.create_text(450,250,text="ack received",font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(ack)
    canvas.delete(ackrec)
    print('Acknowledgement send')
    return
def frame_lost(frame,counter,timer):
    time.sleep(5)
    for i in range(1,25):
        if(i%2 == 0):
            counter = counter+1
            canvas.delete(timer)
            timer = draw_timer(counter)
        time.sleep(0.25)
        canvas.move(frame,5,0)
        canvas.update()
    lost = canvas.create_text(450,250,text="Frame is lost",font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(lost)
    canvas.delete(frame)
    return counter
    print('frame is lost...')
    
def wait_for_event():
    ch = 'y'
    while(ch == 'y'):
        counter = 0
        timer = draw_timer(counter) 
        data = sender_network()
        counter = sender_physical(counter,timer)
        print(counter)
        random = randint(1,4)
        print('receiver random',random)
        ack = draw_ack()
        if(random == 3):
            time.sleep(2)
            acknowledgement_lost(ack,counter,timer)
            print('send same frame again')
            sender_physical(0,timer)
            ack = draw_ack()
            acknowledgement_received(ack,counter,timer)
        else:
            acknowledgement_received(ack,counter,timer)
        ch = input('wanna send more frames..(y/n)')
def draw_frame():
    return canvas.create_rectangle(50,100,120,150,fill='green')
def move_frame(frame,counter,timer):
    for i in range(1,25):
        if(i%2 == 0):
            counter = counter+1
            canvas.delete(timer)
            timer = draw_timer(counter)
            
        time.sleep(0.25)
        canvas.move(frame,30,0)
        canvas.update()
def draw_ack():
    return canvas.create_rectangle(700,100,780,150,fill='red')
def move_ack(ack,counter ,timer):
    for i in range(1,25):
        if(i%2 == 0):
            counter = counter+1
            canvas.delete(timer)
            timer = draw_timer(counter)
            
        time.sleep(0.25)
        canvas.move(ack,-30,0)
        canvas.update()
def draw_timer(counter):
    return canvas.create_text(450,450,text= counter,font="Times 30 italic bold")
wait_for_event()
root.mainloop()
ssss
