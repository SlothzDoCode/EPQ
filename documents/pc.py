import tkinter as tk
from tkinter import *
import socket
from tkinter import messagebox
import threading

#TODO import gTTS to pi
#TODO set up gTTS in pi script

#*server

def Client_connect():
    global client
    
    flagGreen_select.config(state=NORMAL)
    flagYellow_select.config(state=NORMAL)
    flagRed_select.config(state=NORMAL)
    flagBlue_select.config(state=NORMAL)
    PBAlert_btn.config(state=NORMAL)
    close_btn.config(state=NORMAL)
    position_drop.config(state=NORMAL)
    sendPosition_btn.config(state=NORMAL)
    time_drop.config(state=NORMAL)
    sendTimer_btn.config(state=NORMAL)
    PBCloseAlert_btn.config(state=NORMAL)
    Pitstop_btn.config(state=NORMAL)
    try:
        ip = "192.168.1.76" # IP of Raspberry Pi
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 2325))
        print("CLIENT: connected")
    
        msg_startUP = "remove_IP"
        client.send(msg_startUP.encode())

    except:
        messagebox.showerror("..","Unable to connect to dash")
    
#*button commands

def flagGreen_command():
    try: 
        msg_green = "Green flag"
        # send a message
        client.send(msg_green.encode())
    except:
        messagebox.showerror("..","Failed to send to dash")    

def flagYellow_command():
    try:
        msg_yellow = "Yellow flag"
        # send a message
        client.send(msg_yellow.encode())   
    except:
        messagebox.showerror("..","Failed to send to dash")
    
def flagRed_command():
    try:
        msg_red = "Red flag"
        # send a message
        client.send(msg_red.encode())    
    except:    
        messagebox.showerror("..","Failed to send to dash")
        
def flagBlue_command():
    try:
        msg_blue = "Blue flag"
        # send a message
        client.send(msg_blue.encode())  
    except:
        messagebox.showerror("..","Failed to send to dash")      

def shutdown():
    
    
    msg_exit = "exit_server"
    # send a message
    client.send(msg_exit.encode())
    
    # exit
    client.close()
    print("left server")
    exit()

def PB_cmd():
    try:
        msg_PB = "PB_alert"
        # send a message
        client.send(msg_PB.encode())
    except:
        messagebox.showerror("..","Failed to send to dash")       
 
def updatePos_cmd():
    global pos_clicked
    print("value is " + pos_clicked.get())
    
    try:
        msg_posUpdate = str("pos" + " " + pos_clicked.get())
        client.send(msg_posUpdate.encode())
    except:
        messagebox.showerror("..","Failed to send to dash")    

def updateTimer_cmd():
    global time_clicked
    print("value is " + time_clicked.get())
    
    try:
        msg_timerUpdate = str("time" + time_clicked.get())
        client.send(msg_timerUpdate.encode())  
    except:
        messagebox.showerror("..","Failed to send to dash")          

def PBCloseAlert_cmd():
    try:
        msg_PBClose = "PB_close"
        #send a message
        client.send(msg_PBClose.encode())
    except:
        messagebox.showerror("..","Failed to send to dash")
    
def pitstop_cmd():
    try:
        msg_pitstop = "Pitstop"
        #send a message
        client.send(msg_pitstop.encode())
    except:
        messagebox.showerror("..","Failed to send to dash") 
        
def leading_cmd():
    try:
        msg_leadingCar = "leading-" 
        
        client.send(msg_leadingCar.encode())          
    except:
            messagebox.showerror("..","Failed to send to dash")
            
def trailing_cmd():
    try:
        msg_trailingCar = "trailing-" 
        
        client.send(msg_trailingCar.encode())          
    except:
            messagebox.showerror("..","Failed to send to dash")            
    
#*set up visual display 

display = tk.Tk()

flagGreen_select = tk.Button(
    text="green flag",
    width=8,
    height=4,
    command=flagGreen_command,
    bg="#00FF00")
flagGreen_select.grid(row=4, column=4, pady=50, padx=50)

flagYellow_select = tk.Button(
    text="yellow flag",
    width=8,
    height=4,
    command=flagYellow_command,
    bg="#FFFF00")
flagYellow_select.grid(row=4, column=5, pady=50, padx=50)

flagRed_select = tk.Button(
    text="red flag",
    width=8,
    height=4,
    command=flagRed_command,
    bg="#FF0000")
flagRed_select.grid(row=4, column=6, pady=50, padx=50)

flagBlue_select = tk.Button(
    text="Blue flag",
    width=8,
    height=4,
    command=flagBlue_command,
    bg="#399dbc")
flagBlue_select.grid(row=4, column=7, pady=50, padx=50)

PBAlert_btn = tk.Button(
    text = "PB_alert",
    width=9,
    height=4,
    command=PB_cmd)
PBAlert_btn.grid(row=4, column=10, pady=50, padx=50)

close_btn = tk.Button(
    text = "Stop display",
    width=9,
    height=4,
    command=shutdown)
close_btn.grid(row=4, column=11, pady=50, padx=50)

position_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
pos_clicked = StringVar(display)
pos_clicked.set(position_options[0])

position_drop = OptionMenu(display, pos_clicked, *position_options)
position_drop.grid(row=6, column=5, pady=50, padx=50)

sendPosition_btn = tk.Button(
    text="Update current position",
    command=updatePos_cmd)
sendPosition_btn.grid(row=6, column=6, pady=50, padx=50)

PBCloseAlert_btn = tk.Button(
    text="PB Close",
    width=9,
    height=4,
    command=PBCloseAlert_cmd)
PBCloseAlert_btn.grid(row=6, column=10, pady=50, padx=50)

time_options = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
time_clicked = StringVar(display)
time_clicked.set(time_options[0])

time_drop = OptionMenu(display, time_clicked, *time_options)
time_drop.grid(row=8, column=5, pady=50, padx=50)

sendTimer_btn = tk.Button(
    text="Set time remaining",
    command=updateTimer_cmd)
sendTimer_btn.grid(row=8, column=6, pady=50, padx=50)

Pitstop_btn = tk.Button(
    text="Pitstop",
    width=9,
    height=4,
    command=pitstop_cmd)
Pitstop_btn.grid(row=8, column=10, pady=50, padx=50)

timerControl_display = tk.Label(text="")
timerControl_display.grid(row=10, column=5, pady=50, padx=50)

leadingCar_ent = tk.Entry()
leadingCar_ent.grid(row=10, column=6, pady=50, padx=50)

leadingCar_ent.bind(leading_cmd(leadingCar_ent.get()))


#*start-up

threading.Thread(target=Client_connect).start()

display.attributes('-fullscreen', True)
#//display.attributes('-topmost', True)
display.mainloop()
