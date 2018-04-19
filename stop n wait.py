from tkinter import *
from random import *
import time
def sender_network():
    frame = input('enter data: ')
    return frame
    
def sender_physical(frame):
    #print('data received at physical layer of sender...')
    random = randint(1,4)
    print('sender random',random)
    if(random == 3):
        time.sleep(3)
        frame_lost()
        print('send same again')
        sender_physical(frame)
    else:
        receiver()
        return

def receiver():
    print('data received at physical layer of receiver...')
    return 

def acknowledgement_lost():
    print('Acknowledgement lost')
    return

def acknowledgement_received():
    print('Acknowledgement send')
    return
def frame_lost():
    print('frame is lost...')
    
def wait_for_event():
    ch = 'y'
    while(ch == 'y'):
        frame = sender_network()
        sender_physical(frame)
        random = randint(1,4)
        print('receiver random',random)
        if(random == 3):
            time.sleep(3)
            acknowledgement_lost()
            print('send same frame again')
            sender_physical(frame)
        else:
            acknowledgement_received()
        ch = input('wanna send more frames..(y/n)')
wait_for_event()
