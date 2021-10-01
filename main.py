import socket
from threading import Thread

ClientMultiSocket = socket.socket()
host = '10.4.1.144'
port = 6969

print('Waiting for connection response')


def thread_receive():
    print('hello')
    while True:
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))


try:
    ClientMultiSocket.connect((host, port))
#    start_new_thread(thread_receive(), ())
    t= Thread(target = thread_receive)
    t.start()
    print('23')
    while True:
        Input = input('Hey there: ')
        ClientMultiSocket.sendall(Input.encode('utf-8'))
        print('message send')
 #       print(res.decode('utf-8'))

except socket.error as e:
    print(str(e))

ClientMultiSocket.close()
