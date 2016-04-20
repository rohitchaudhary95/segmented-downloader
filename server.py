import asyncore
import socket
import time
import thread
from time import *
import threading, urllib2,urllib
import Queue
import sys
from Tkinter import *
import tkFileDialog, Tkconstants
import os
import ttk
from urllib2 import Request, HTTPError, URLError
import httplib
import tkMessageBox
import pygame,random,copy;
from pygame.locals import *;
no_of_connections=0
no_of_acceptance=0
start_flag = False;
connect_flag = False;


win = Tk()
win.title('Alpha++')
def run_thread(a) :
  asyncore.loop()

def call():
  execfile("youtube.py")
  
def call2():
  execfile("pong.py")
  
def call3():
  execfile("c.py")
  
def call4():  
  os.system("Rundll32.exe User32.dll,LockWorkStation") 

  
class GuiPart:
  def __init__(self, master, queue, endCommand):
    self.queue = queue


    # Set up the GUI
    #.Frame.__init__(self, master)

    # options for buttons
    #button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    """
    self.L1 = Label(master, text="URL")
    self.L1.grid( row=0, column=0, sticky = W, padx=10, pady=10)
    
    self.E1 = Entry(master, bd =5,width=50)
    self.E1.grid( row=0, column=1, columnspan = 1, padx=10, pady=10)
    
    self.L2 = Label(master, text="Destination path")
    self.L2.grid( row=1, column=0, sticky = W, padx=10, pady=10)

    self.v = StringVar()
    self.E2 = Entry(master, bd =5,textvariable=self.v,width=50)
    self.E2.grid( row=1, column=1, padx=2, pady=10)
    
    self.B1=Button(master, text='Browse', command=self.askdirectory,bd=2)
    self.B1.grid( row=1, column=2, padx=6, pady=0, sticky= E )

    self.L3 = Label(master, text="Available Clients")
    self.L3.grid( row=2, column=0, sticky = W, padx=10, pady=10)
    
    

    self.Li1= Listbox(master,width=50,selectmode=MULTIPLE,height=4)
    self.Li1.grid( row=2, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
    self.Li1.insert(1, "Python")
    self.Li1.insert(2, "Perl")
    self.Li1.insert(3, "C")
    self.Li1.insert(4, "PHP")
    self.Li1.insert(5, "JSP")
    self.Li1.insert(6, "Ruby")
    

    self.s = ttk.Scrollbar(master, orient=VERTICAL, command=(self.Li1).yview)
    self.s.grid(column=2, row=2, sticky=(W,N,S))
    self.Li1['yscrollcommand'] = self.s.set
    #ttk.Sizegrip().grid(column=2, row=2, sticky=(S,E))
     

    self.B2=Button(master, text='Connect')
    self.B2.grid( row=3, column=1, padx=4, pady=10 )


    self.L4 = Label(master, text="Connected Clients")
    self.L4.grid( row=4, column=0, sticky = W, padx=10, pady=10)
    

    self.Li2= Listbox(master,width=50,height=4)
    self.Li2.grid( row=4, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
    self.Li2.insert(1, "Python")
    self.Li2.insert(2, "Perl")
    self.Li2.insert(3, "C")
    self.Li2.insert(4, "PHP")
    self.Li2.insert(5, "JSP")
    self.Li2.insert(6, "Ruby")

    self.s1 = ttk.Scrollbar(master, orient=VERTICAL, command=(self.Li2).yview)
    self.s1.grid(column=2, row=4, sticky=(W,N,S))
    self.Li2['yscrollcommand'] = self.s1.set
    #ttk.Sizegrip().grid(column=2, row=4, sticky=(S,E))

    self.B3=Button(master, text='Start Download',command=self.start)
    self.B3.grid( row=5, column=1, padx=4, pady=10 )


    # defining options for opening a directory
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'Select Location:'

    self.progress = ttk.Progressbar(master, orient="horizontal", 
                    length=200, mode="determinate")
    self.progress.grid(row=6, column=1, padx=4, pady=10)

    self.bytes = 0
    self.maxbytes = 0
    self.master=master
    #self.endCommand=endCommand


    """

    self.L1 = Label(master, text="URL")
    self.L1.grid( row=0, column=0, sticky = W, padx=10, pady=10)

    self.urlentered = StringVar()
    self.urlbox = Entry(master,textvariable=self.urlentered,bd=5,width=50,background="lightyellow")
    self.urlbox.grid( row=0, column=1, padx=2, pady=10)

    self.L2 = Label(master, text="Destination path")
    self.L2.grid( row=1, column=0, sticky = W, padx=10, pady=10)

    self.v = StringVar()
    self.E2 = Entry(master, bd =5,textvariable=self.v,width=50,background="lightyellow")
    self.E2.grid( row=1, column=1, padx=2, pady=10)


    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = master
    options['title'] = 'Select Location:'


    self.B1=Button(master, text='Browse',background="pink", command=self.askdirectory,bd=2)
    self.B1.grid( row=1, column=2, padx=6, pady=0, sticky= E )

    
    self.L10 = Label(master, text="                                  Entertainment                                                   ",background="lightgreen")
    self.L10.grid( row=6, column=1, sticky = W, padx=0, pady=10)
	
    self.L11 = Label(master, text="                                        ",background="lightgreen")
    self.L11.grid( row=6, column=0, sticky = W, padx=0, pady=0)
	
    self.L12 = Label(master, text="                          ",background="lightgreen")
    self.L12.grid( row=6, column=2, sticky = W, padx=0, pady=0)
	
    self.B12 = Button(master, text="File Send",background="lightblue", command=call3)
    self.B12.grid( row=7, column=0, padx=0, pady=0,)
    
    self.B10 = Button(master, text="Youtube Downloader",background="lightblue",command=call)
    self.B10.grid( row=8, column=0, padx=0, pady=0,)

    self.B11 = Button(master, text="Pong Game",background="lightblue", command=call2)
    self.B11.grid( row=7, column=2, padx=0, pady=0,)
    
    self.B12 = Button(master, text="Lock Screen",background="lightblue", command=call4)
    self.B12.grid( row=8, column=2, padx=5, pady=6,)
	
    self.L3 = Label(master, text="Available Clients")
    self.L3.grid( row=2, column=0, sticky = W, padx=10, pady=10)

    #sb = Scrollbar(win,orient=VERTICAL)

    self.lb1 = Listbox(master,height=5,width=50,selectmode=MULTIPLE,background="lightyellow")
    self.lb1.grid( row=2, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
    #self.lb1.insert(1,"List of connections available")

    self.s = ttk.Scrollbar(master, orient=VERTICAL, command=(self.lb1).yview)
    self.s.grid(column=2, row=2, sticky=(W,N,S))
    self.lb1['yscrollcommand'] = self.s.set

    #sb.configure(command=lb1.yview)
    #lb1.configure(yscrollcommand=sb.set)

    self.L4 = Label(master, text="Connected Clients")
    self.L4.grid( row=4, column=0, sticky = W, padx=10, pady=10)

    self.B2=Button(master, text='Connect',command=self.start_pushed,background="pink")
    self.B2.grid( row=3, column=1, padx=4, pady=10 )

    
    self.lb2 = Listbox(master,height=5,width=50,selectmode=MULTIPLE,background="lightyellow")
    self.lb2.grid( row=4, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
    #self.lb2.insert(1,"List of accepted connections")

    self.s1 = ttk.Scrollbar(master, orient=VERTICAL, command=(self.lb2).yview)
    self.s1.grid(column=2, row=4, sticky=(W,N,S))
    self.lb2['yscrollcommand'] = self.s1.set


    

    self.B3=Button(master, text='Start Download',command=self.start_download,background="pink")
    self.B3.grid( row=5, column=1, padx=4, pady=10 )

    self.progress = ttk.Progressbar(master, orient="horizontal", 
                    length=200, mode="determinate")
    #self.progress.grid(row=6, column=1, padx=4, pady=10)

    self.bytes = 0
    self.maxbytes = 0
    self.master=master
    self.progress['value']=0
    self.progress["maximum"] = 55238




  def askdirectory(self):

    #Returns a selected directoryname.    
    #print (self.E1).get()
    (self.v).set(tkFileDialog.askdirectory(**self.dir_opt)) 
    
  def start_download(self):
    #print "here in start"
    global start_flag, should_proceed
    start_flag = True
    should_proceed=True
    #self.start()

  def start_pushed(self):

    if len(self.urlentered.get())!=0 and len(self.v.get())!=0:
      try:
        temp=urllib.urlopen(self.urlentered.get())
      except:
        #print e.code
        print "\n\n-----URL invalid------\n\n"
        tkMessageBox.showinfo("Error", "URL invalid")
      else:
        global connect_flag
        connect_flag = True
    else:
      print "\n\n-----URL and directory can't be empty------\n\n"
      tkMessageBox.showinfo("Error", "URL and directory can't be empty")
 

  def threader(self):
    self.thread2 = threading.Thread(target=self.start)
    self.thread2.start()


  def start(self):
    global server

    self.progress["value"] = 0
    self.maxbytes = server.clients_handler[0].sizeToDownload
    self.progress["maximum"] = server.clients_handler[0].sizeToDownload
    #self.read_bytes()


  def read_bytes(self,i):
    '''simulate reading 500 bytes; update progress bar'''
    #global server
    print "\n\n----here",i,"  ",server.clients_handler[i].downloadedTillNow,"---\n\n"
    self.bytes = server.clients_handler[i].downloadedTillNow
    self.progress["value"] = self.bytes
    if self.bytes < 55238:
      # read more bytes after 100 ms
      self.master.after(1000, self.read_bytes(i))
    #else:
    #   self.endCommand()

    # Add more GUI stuff here

  def processIncoming(self):
    """
    Handle all the messages currently in the queue (if any).
    """
    while self.queue.qsize():
      try:
        msg = self.queue.get(0)
        # Check contents of message and do what it says
        # As a test, we simply print it
        #print msg
      except Queue.Empty:
        pass

class ThreadedClient:
  """
  Launch the main part of the GUI and the worker thread. periodicCall and
  endApplication could reside in the GUI part, but putting them here
  means that you have all the thread controls in a single place.
  """
  def __init__(self, master):
    """
    Start the GUI and the asynchronous threads. We are in the main
    (original) thread of the application, which will later be used by
    the GUI. We spawn a new thread for the worker.
    """
    self.master = master

    # Create the queue
    self.queue = Queue.Queue()

    # Set up the GUI part
    self.gui = GuiPart(master, self.queue, self.endApplication)

    # Set up the thread to do asynchronous I/O
    # More can be made if necessary
    self.running = 1
    #self.thread1 = threading.Thread(target=self.workerThread1)
    #self.thread1.start()

    # Start the periodic call in the GUI to check if the queue contains
    # anything
    self.periodicCall()

  def periodicCall(self):
    """
    Check every 100 ms if there is something new in the queue.
    """
    self.gui.processIncoming()
    if not self.running:
      # This is the brutal stop of the system. You may want to do
      # some cleanup before actually shutting it down.
      import sys
      sys.exit(1)
    self.master.after(100, self.periodicCall)

  def workerThread1(self):
    """
    This is where we handle the asynchronous I/O. For example, it may be
    a 'select()'.
    One important thing to remember is that the thread has to yield
    control.
    """
    while self.running:
      # To simulate asynchronous I/O, we create a random number at
      # random intervals. Replace the following 2 lines with the real
      # thing.
      sleep(2 * 0.3)
      msg = 2
      self.queue.put(msg)

  def endApplication(self):
    #print "hey"
    self.running = 0













"""def askdirectory():
  return v.set(tkFileDialog.askdirectory(**dir_opt))"""


 


count_conn = 0

def run_thread_gui(a) :
  global client
  client = ThreadedClient(win)
  
  win.mainloop()


'''
L1.pack()
urlbox.pack()
L2.pack()
E2.pack()
B1.pack()
L3.pack()
sb.pack(side=RIGHT,fill=Y)
lb1.pack(side=LEFT)
'''









class EchoHandler(asyncore.dispatcher_with_send):

  def __init__(self,conn_sock, client_address,count_conn):
    self.CA = client_address
    self.cl_no=count_conn
    self.DATA = ''
    self.sizeToDownload=0
    self.acceptance=-1
    self.out_buffer = ''
    self.BUFFER = 1024
    self.is_writable = False
    self.sock = conn_sock
    asyncore.dispatcher.__init__(self, conn_sock)
    self.downloadedTillNow=0
    self.started=0
  ''' handles incoming data from client
  EchoServer.clients[self.sock] will give the addr of client where
  data is coming from '''
  
  def handle_read(self):
    data = self.recv(1024*1024)
    if data:
      if self.acceptance==3:
        self.DATA+=data
      if data=="Sending data":
        self.acceptance=3
      if self.acceptance==2:
        self.downloadedTillNow+=int(data)
        print "\n---------Client ",self.cl_no," -- Downloaded till now = ",self.downloadedTillNow,"----\n"
        if self.started==0 :
          self.started=1
          """client.progress["value"] = 0
          client.maxbytes =self.sizeToDownload
          client.progress["maximum"] = self.sizeToDownload"""
          #client.gui.read_bytes(self.cl_no-1)
      if data=="acceptance=1":
        self.acceptance=1
      if data=="acceptance=0":
        self.acceptance=0

      #self.send(data)
      #print "received following data from : "
      #print EchoServer.clients[self.sock]
      #print repr(data)


class EchoServer(asyncore.dispatcher):

  clients = {} # a dictionary of clients where sockets are keys and addr are values
  clients_handler = []

  def __init__(self, host, port):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.set_reuse_addr()
    self.bind((host, port))
    self.listen(5)
    self.obuffer = []
        
  # handles incoming client connections   
  def handle_accept(self):
    pair = self.accept()
    if pair is None:
      pass
    else:
      sock, addr = pair
      EchoServer.clients[sock] = addr
      global lb1,count_conn
      count_conn = count_conn + 1
      client.gui.lb1.insert(count_conn,repr(addr))
      print 'Incoming connection from %s' % repr(addr)
      handler = EchoHandler(sock,addr,count_conn) # call the echohandler class defined above to handle the incoming data and other stuff
      EchoServer.clients_handler.append(handler)

  def handle_connect(self):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('', 8080))


  # Pass a string data as argument to be sent to client
  # cl_no represents client no. to whom data is to be sent
  def write(self,cl_no,data):
    if len(EchoServer.clients_handler)>cl_no:
      EchoServer.clients_handler[cl_no].send(data)
    else:
      print "\nNo client connected\n"

  def getListOfClients(self):
    print "connected clients are : "
    for x in self.clients:
      print self.clients[x]






server = EchoServer('127.0.0.1', 8080)

if __name__ == "__main__": # Start the server in a new thread
  thread.start_new_thread(run_thread,("erte",) )
  thread.start_new_thread(run_thread_gui,("erte",) )






print "waiting for connections...\n"
st=time();
while True:
  
  sleep(3)
  if len(EchoServer.clients)>no_of_connections:
    no_of_connections=len(EchoServer.clients)
    #server.getListOfClients()
    #server.write(0,"Server data")
    #server.write(1,"Server data")
  if  connect_flag==True:
    break
    '''try:
    pass
  except:
    print "Exited thread\n"'''


#url = "http://kaz.dl.sourceforge.net/project/sevenzip/7-Zip/9.20/7z920.exe"
url = client.gui.urlentered.get()

print "\nurl entered is " + url + "\n"

os.chdir(client.gui.v.get())

file_name = url.split('/')[-1]

f = open(file_name, 'wb')

u = urllib2.urlopen(url)

meta = u.info()





#checking if url is empty






def download(i):
  if i==0:
    start=0
  else:        
    start=i*packet_size_each_thread[i-1]
  start1=str(start)
  end=start+packet_size_each_thread[i]-1
  end1=str(end)
  req = urllib2.Request(url, headers={'Range':'bytes='+start1+'-'+end1})
  u = urllib2.urlopen(req)
  block_sz = 8192
  file_size_dl = start
  temp='\0'
  while True:
    data=u.read(block_sz)
    if not data:
      break
    print('%d Fetched %s from %s' % (i,len(data), url))
    temp=temp+data
    
  temp=temp[1:]
  print "\n\n"
  print len(temp),"\n\n"
  f.seek(start)
  f.write(temp)


def start_parallel():
  #result = Queue.Queue()
  threads = [threading.Thread(target=download, args = (i,)) for i in range(no_of_threads)]
  for t in threads:
    t.start()
  for t in threads:
    t.join()

 
items = map(int, client.gui.lb1.curselection())
print items

#sending requests to all selected clients if they interested in download
i=0
while i<no_of_connections:
  if i in items:
    server.write(i,"Would you help me in download of "+url)
  i+=1

#waiting for requests to be responded
print "\n\n--------waiting for clients to respond--------\n\n"

while True:
  no_of_responses=0
  #no_of_acceptance=0
  i=0
  while i < no_of_connections:
    if server.clients_handler[i].acceptance!=-1:
        no_of_responses+=1
    if server.clients_handler[i].acceptance==1:
        server.clients_handler[i].acceptance=2

        no_of_acceptance+=1
        server.write(i,str(no_of_acceptance))
        #global lb2
        
        client.gui.lb2.insert(no_of_acceptance,repr(server.clients_handler[i].CA))
    i+=1
  if no_of_responses==len(items):
    break
  sleep(2)


file_size = int(meta.getheaders("Content-Length")[0])


print  "file size total is  -------------",file_size,"----------"
print "no of acceptance is --------------",(no_of_acceptance),"------------"

packet_size_server=file_size/(no_of_acceptance+1)


packet_size_each_client=[]

i=0
cnt=0
while i<no_of_connections:
  if server.clients_handler[i].acceptance==2:
    cnt+=1
    if cnt!=no_of_acceptance:
      packet_size_each_client.append(file_size/(no_of_acceptance+1))
    else:
      packet_size_each_client.append((file_size/(no_of_acceptance+1)) + (file_size%(no_of_acceptance+1)))
  else:
    packet_size_each_client.append(0)
  i+=1


#waiting for download button to be pressed
should_proceed=False

while should_proceed==False:
  sleep(2)


#sending details to those who accepted
i=0
start_from=packet_size_server
while i<no_of_connections:
  if server.clients_handler[i].acceptance==2:
    server.write(i,url)
    server.clients_handler[i].sizeToDownload=packet_size_each_client[i]
    server.write(i,str(start_from))
    
    print i+1," starts from ",start_from,"and downloads ",packet_size_each_client[i]
    sleep(1)
    sleep(1)
    start_from+=packet_size_each_client[i]
    server.write(i,str(packet_size_each_client[i]))
  i+=1


print "\n\n"

no_of_threads=2
packet_size_each_thread=[]
i=0
while i<no_of_threads:
  if i != no_of_threads-1:
    packet_size_each_thread.append(packet_size_server/no_of_threads)
  else:
    packet_size_each_thread.append((packet_size_server/no_of_threads) + (packet_size_server%no_of_threads))
  i+=1




st=time()

# start_parallel is starting download of own
start_parallel()
print time()-st



# wait for clients to send downloaded data
print "\n\n --------waiting for clients to send downloaded data------\n\n"

while True:
  completed_downloads=0
  i=0
  while i < no_of_connections:
    if server.clients_handler[i].acceptance==3:
      if len(server.clients_handler[i].DATA)==server.clients_handler[i].sizeToDownload:
        completed_downloads+=1
    i+=1
  if completed_downloads==no_of_acceptance:
    break
  sleep(2)


main_data='\0'
i=0

while i<no_of_connections:
  if server.clients_handler[i].acceptance==3:
    main_data+=server.clients_handler[i].DATA
  i+=1

main_data=main_data[1:]
#print len(main_data)
start=packet_size_server
print "\n\n------total data recieved from rest = ",len(main_data),"-----------\n\n"
f.seek(start)
f.write(main_data)
f.close()

print "\n\n-------Task completed :)-----\n\n"


#to keep the cmd on
while True:
  a=1



   
