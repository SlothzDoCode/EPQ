import socket
import tkinter as tk
import threading
import time

#var's

host = '192.168.1.76'
port = 2325

current_bg = "black"

fg_dark = "black"
fg_light = "white"

positions = ["pos 1","pos 2","pos 3","pos 4","pos 5","pos 6","pos 7","pos 8","pos 9","pos 10","pos 11","pos 12","pos 13","pos 14","pos 15","pos 16"]
countdown_timer = ["time5","time10","time15","time20","time25","time30","time35","time40","time45","time50","time55","time60","time65","time70","time75","time80","time85","time90","time95"]

current_pos = "0"

listener_limit = 1

def main():
  global current_pos
  global positions
  global current_bg
  global fg_dark
  global fg_light
  
  serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    serv.bind((host,port))
    print("Running ther server on {}, {}".format(host,port))
  except:
    print("Unable to bind host to {} and port {}".format(host,port))

  serv.listen(listener_limit)

  while 1:
    conn, addr = serv.accept()
    from_client = ''
    print("Successfully connected to client {} {}".format(addr[0], addr[1]))

    while True:
      data = conn.recv(4096).decode()
      if not data: break
      from_client += data
      from_client = str(from_client)
      print(type(from_client))
      print("Recieved: " + from_client)

      if from_client == "Green flag":
        current_bg = "green"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg, fg=fg_light)
        timer_lbl.configure(bg=current_bg, fg=fg_light)
      
      elif from_client == "Yellow flag":
        current_bg = "yellow"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg, fg=fg_dark)
        timer_lbl.configre(bg=current_bg, fg=fg_dark)
        
      elif from_client == "Red flag":
        current_bg = "red"
        diplay.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg, fg=fg_light)
        timer_lbl.configure(bg=current_bg, fg=fg_light)
      
      elif from_client == "Blue flag":
        current_bg = "blue"
        display.configure(bg=current_bg)
        position_lbl.configure(bg=current_bg, fg=fg_light)
        timer_lbl.configure(bg=current_bg, fg=fg_light)
      
      elif from_client == "PB_alert":
        display.configure(bg="#a28834")
        position_lbl.configure(bg="#a28834", fg=fg_dark)
        position_lbl.configure(bg="'a28834", fg=fg_dark)
      
      elif from_client == "PB_close":
        ()
      
      elif from_client in positions:
        current_pos = from_client
        position_lbl.configure(text=current_pos)
        
      elif from_client in countdown_timer:
        countdown_time = int(from_client[4:])
        def countdown(count):
          timer_lbl.configure(text=round(count, 2))
          
          if count > 0:
            timer_lbl.after(1000, countdown, count-0.01)

        countdown(countdown_time)
      
      elif from_client == "exit_server":
        display.destroy()
        exit()
      
      from_client = ''

if __name__ == '__main__':
  display = tk.Tk()
  display.configure(bg-current_bg)
  threading.Thread(target=main).start()

  position_lbl = tk.Label()
