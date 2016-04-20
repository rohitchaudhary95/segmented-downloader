import socket
import threading, urllib2
import Queue
import sys
from time import *
import asyncore



    



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))



request_to_download=client_socket.recv(8812)
print request_to_download
print "1.Yes\n0.No"

choice=raw_input()

if choice=='1':
    response="acceptance=1"
else:
    response="acceptance=0"

client_socket.send(response)

if choice=='1':
    client_no=int(client_socket.recv(8812))
no_of_threads=2
#client_no=1

if choice=='1':

    url = client_socket.recv(8812)
    start_from=int(client_socket.recv(8812))
    packet_size_each_client=int(client_socket.recv(8812))

    print "\n\n------amount to download= ",packet_size_each_client,"--------\n\n"   
    
    packet_size_each_thread=[]
    i=0
    while i<no_of_threads:
        if i != no_of_threads-1:
            packet_size_each_thread.append(packet_size_each_client/no_of_threads)
        else:
            packet_size_each_thread.append((packet_size_each_client/no_of_threads) + (packet_size_each_client%no_of_threads))
        i+=1
    
    #print packet_size_each
    u = urllib2.urlopen(url)

    main_data=[]
    main_data.append([])
    main_data.append([])

    #suppose this is client 1




    def download(i):
        
        x=client_no*no_of_threads
        if i==x:
            start=start_from
        else:
            start=start_from + (i-(x))*packet_size_each_thread[i-(x)-1]
        start1=str(start)
        end=start+ packet_size_each_thread[i-(x)]-1
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
            client_socket.send(str(len(data)))
            #f.seek(file_size_dl)
            #ile_size_dl += len(data)
            #f.write(data)
        
        main_data[i-x]=temp[1:]
        #sock.send(temp)
        #print len(temp)
        #f.seek(start)
        #f.write(temp)

        

    def start_parallel():
        #result = Queue.Queue()
        x=client_no*no_of_threads
        y=x+no_of_threads

        threads = [threading.Thread(target=download, args = (i,)) for i in range(x,y)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        




    st=time()
    start_parallel()
    print time()-st

    print "\n\n------sending data-----\n\n"
    client_socket.send("Sending data")
    for i in range(2):
        print len(main_data[i])
        client_socket.send(main_data[i])
    print "\n\n----completed-----\n\n"
    #time.sleep(2)
        
    '''data = client_socket.recv(512)
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print "RECIEVED:" , data
        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data <> 'Q' and data <> 'q'):
            client_socket.send(data)
        else:
            client_socket.send(data)
            client_socket.close()
            break;'''

    #to keep the cmd on
    while True:
        a=1
