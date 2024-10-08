# Author: Abhishek
# Mail: abhishekshukla9586@gmail.com

import socket
import base64
import logging

# Configuration
PORT = 65432  # Non-standard port where the server will listen for incoming connections

# Set up logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(conn):
    """
    Handle communication with a single client connection.

    Args:
        conn (socket.socket): The socket object representing the client connection.
    """
    with conn:
        # Print and log the address of the client that has connected
        client_address = conn.getpeername()
        logging.info(f'Connected by {client_address}')
        print('Connected by', client_address)
        
        while True:
            # Receive data from the client, up to 1024 bytes
            data = conn.recv(1024).decode()
            
            # Break the loop if no data is received (client has disconnected)
            if not data:
                logging.info(f'Client {client_address} disconnected.')
                break
            
            # Split the received data into command and payload
            command, payload = data.split(' ', 1)
            
            # Process the command
            if command == 'BASE64':
                # Encode the payload in base64
                response = base64.b64encode(payload.encode()).decode()
            elif command == 'UPPERCASE':
                # Convert the payload to uppercase
                response = payload.upper()
            else:
                # Handle unknown commands
                response = 'Unknown command'
                logging.warning(f'Unknown command received: {command}')
            
            # Log the received data and the response being sent
            logging.info(f'Received data: {data}')
            logging.info(f'Sending response: {response}')
            
            # Send the response back to the client
            conn.sendall(response.encode())

def server():
    """
    Start the server, listen for incoming connections, and handle each client connection.
    """
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind(('0.0.0.0', PORT))
        
        # Enable the server to accept incoming connections
        s.listen()
        
        # Print and log a message indicating that the server has started
        logging.info(f'Server started on port {PORT}')
        print(f'Server started on port {PORT}')
        
        while True:
            # Accept a new client connection
            conn, addr = s.accept()
            
            # Handle the client connection
            handle_client(conn)

# Execute the server function if this script is run directly
if __name__ == '__main__':
    server()

