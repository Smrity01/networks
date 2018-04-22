from tkinter import *
from random import *
import time

root = Tk()
root.title('Stop and Wait')
canvas = Canvas(root, width=900, height=500)
canvas.pack()
canvas.create_text(100, 50, text="Sender", font="Times 20 italic bold")
canvas.create_text(800, 50, text="Receiver", font="Times 20 italic bold")


def sender_network():
    frame = [1,2,3,4,5]
    return frame


def sender_physical(counter):
    frame = draw_frame()
    random = randint(1, 4)
    #print('Sender random', random)
    if (random == 3):
        time.sleep(0.5)
        frame_lost(frame, counter)
        print('Frame lost, sending same again...')
        sender_physical(0)
    else:
        counter = move_frame(frame, counter)
        receiver(frame)
    return int(counter)


def frame_lost(frame, counter):
    time.sleep(5)
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            # print("counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(frame, 5, 0)
        canvas.update()
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            # print("counter: ", counter)
            canvas.update()
        time.sleep(0.25)
    lost = canvas.create_text(450, 250, text="Frame is lost and timeout...", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(lost)
    canvas.delete(frame)
    print('Frame is lost...')
    return


def receiver(frame):
    framereceived = canvas.create_text(450, 250, text="Frame Received.", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(framereceived)
    canvas.delete(frame)
    print('Data received at physical layer of receiver...')
    return


def acknowledgement_received(ack, counter):
    move_ack(ack, counter)
    ackrec = canvas.create_text(450, 250, text="Ack Received. Ready for next frame.", font="Times 15 italic bold")
    canvas.update()
    time.sleep(2)
    canvas.delete(ack)
    canvas.delete(ackrec)
    print('Acknowledgement sent')
    return


def acknowledgement_lost(ack, counter):
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(ack, -7, 0)
        canvas.update()
    acklost = canvas.create_text(450, 250, text="Time out...! Acknowledge Lost, send the same frame again", font="Times 15 italic bold")
    canvas.update()
    time.sleep(1)
    canvas.delete(acklost)
    canvas.delete(ack)
    print('Acknowledgement lost.')
    return

def wait_for_event(counter):

    data = sender_network()
    for i in data:
        counter = int(sender_physical(0))
        #print("Counter value in wait for event", counter)
        random = randint(1, 4)
        ack = draw_ack()
        if (random == 3):
            time.sleep(0.25)
            acknowledgement_lost(ack, counter)
            print('Sending same frame again...')
            counter = int(sender_physical(0))
            ack = draw_ack()
            acknowledgement_received(ack, counter)
        else:
            acknowledgement_received(ack, counter)


def draw_frame():
    return canvas.create_rectangle(50, 100, 120, 150, fill='green')


def move_frame(frame, counter):
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(frame, 30, 0)
        canvas.update()
    return counter


def draw_ack():
    return canvas.create_rectangle(700, 100, 780, 150, fill='red')


def move_ack(ack, counter):
    for i in range(1, 25):
        if (i % 2 == 0):
            counter = counter + 1
            canvas.itemconfig(timer, text=counter)
            #print("Counter: ", counter)
            canvas.update()
        time.sleep(0.25)
        canvas.move(ack, -28, 0)
        canvas.update()
    return counter


counter = 0
timer = canvas.create_text(450, 450, text="Timer", font="Times 30 italic bold")
wait_for_event(counter)
root.mainloop()
