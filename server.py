#Author : Abhishek
#Mail : abhishekshukla9586@gmail.com

import socket
import base64

# Configuration
PORT = 65432  # Non-standard port

def handle_client(conn):
    with conn:
        print('Connected by', conn.getpeername())
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, payload = data.split(' ', 1)
            if command == 'BASE64':
                response = base64.b64encode(payload.encode()).decode()
            elif command == 'UPPERCASE':
                response = payload.upper()
            else:
                response = 'Unknown command'
            conn.sendall(response.encode())

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', PORT))
        s.listen()
        print(f'Server started on port {PORT}')
        while True:
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == '__main__':
    server()

