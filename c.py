import socket
import sys
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

f_name = os.path.basename(filename)

if len(filename) > 1 :
    print('Trying to connect...')
    s = socket.socket()
    s.connect(('192.168.43.72', 1234))

    print('Connected. Wating for command.')
    while True:
        cmd = s.recv(32)

        if cmd == 'getfilename':
            print('"getfilename" command received.')
            s.sendall(f_name)

        if cmd == 'getfile':
            print('"getfile" command received. Going to send file.')
            with open(filename, 'rb') as f:
                data = f.read()
            s.sendall('%16d' % len(data))
            s.sendall(data)
            print('File transmission done.')

        if cmd == 'end':
            print('"end" command received. Teminate.')
            break