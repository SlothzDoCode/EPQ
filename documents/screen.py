from flask import *
from flask_socketio import SocketIO
from flask_cors import CORS
import tkinter as tk
from tkinter import *
import threading

#* global vars

current_bg = "black"

fg_dark = "black"
fg_light = "white"

positions = ["pos 1","pos 2","pos 3","pos 4","pos 5","pos 6","pos 7","pos 8","pos 9","pos 10","pos 11","pos 12","pos 13","pos 14","pos 15","pos 16"]
countdown_timer = ["time5","time10","time15","time20","time25","time30","time35","time40","time45","time50","time55","time60","time65","time70","time75","time80","time85","time90","time95"]

current_pos = "0"      

#* tkinter gui  
        
def tkinter_setup():
    global display
    global position_lbl
    global timer_lbl
    display = tk.Tk()
    display.configure(bg=current_bg)
    
    position_lbl = tk.Label(
        bg=current_bg,
        fg="white",
        text=current_pos,
        width=8,
        font=("Arial", 60))
    position_lbl.place(x=400,y=300)

    timer_lbl = tk.Label(
        bg=current_bg,
        fg="white",
        text="",
        width=8,
        font=("Arial", 60))
    timer_lbl.place(x=300,y=50)

    display.attributes('-fullscreen',True)
    display.mainloop()


#* flask + socketio connection

app= Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('ControllerFrontend.html')

@socketio.on('flag_status')
def handle_flag(data):
    print("Flag status:", data) 
    
    if data == "Green Flag":
        current_bg = "green"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg, fg=fg_light)
        timer_lbl.configure(bg=current_bg, fg=fg_light)
        
    elif data == "Yellow Flag":
        current_bg = "yellow"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg,fg=fg_dark)
        timer_lbl.configure(bg=current_bg,fg=fg_dark)
                 
    elif data == "Red Flag":
        current_bg = "Red"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg,fg=fg_light)
        timer_lbl.configure(bg=current_bg,fg=fg_light)
             
    elif data == "Blue Flag":
        current_bg = "blue"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg,fg=fg_light)
        timer_lbl.configure(bg=current_bg,fg=fg_light)
 
    elif data == "PB":
        display.configure(bg="#a28834")
        position_lbl.configure(bg="#a28834", fg=fg_dark)
        timer_lbl.configure(bg="#a28834", fg=fg_dark)    
        
    elif data == "Pitstop":
        display.configure(bg="#c115d4")
        position_lbl.configure(bg="#c115d4", fg=fg_dark)
        timer_lbl.configure(bg="#c115d4", fg=fg_dark)         
    
    elif data in positions:
        current_pos = data
        position_lbl.configure(text=current_pos)
        
    elif data in countdown_timer:
        countdown_time = int(data[4:])
        def countdown(secs):
          mins = secs // 60
          cusec = secs % 60
          timer_lbl.config(text="{}:{:02}".format(mins, cusec))

          if secs > 0:
            timer_lbl.after(1000, countdown, secs - 1)

        countdown(countdown_time*60)    
    
    elif data == "Shutdown":
        display.destroy()
        exit()
    
if __name__ == "__main__":
    
    threading.Thread(target=tkinter_setup, daemon=True).start()    
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, use_reloader=False)
