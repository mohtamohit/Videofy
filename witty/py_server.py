import socket
import sys,os
import sys, json, os
from moviepy.editor import *
import time


#socket connection initializing 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= '127.0.0.1'
port=int(2000)

s.bind((host,port))

def creating_connection():
	s.listen(1)
	conn,addr =s.accept()
	print (conn,addr)
	
	data=conn.recv(100000)
	data=data.decode("utf-8")
	s.close


#connect for rediret when video rendering completed
def conn_for_redirect(txt):
    f = open("con.txt",'w')
    f.write(txt)
    f.close()

#creating or editing video
def creating_video():
	
	conn_for_redirect("0")
	try:
		os.system('sudo python3 videofy.py')
		print("vedio rendring has been completed!")
	except:
		print("Wrong URL or problem in *vediofy.py*")

	conn_for_redirect("1")
while 1:
	creating_connection()
	creating_video()
	
	

	

	