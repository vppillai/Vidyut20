import socket

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    while 1:
        data = s.recv(1024)
        if data == b'':
            break
        print ("Received:", repr(data))
    print ("Connection closed.")
    s.shutdown(socket.SHUT_WR)
    s.close()
    
def main():
    netcat("google.com",80,b'GET /index.html\r\n\r\n')

if __name__=='__main__':
    main()