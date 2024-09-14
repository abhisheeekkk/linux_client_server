# Author: Abhishek
# Mail: abhishekshukla9586@gmail.com

import socket

# Configuration
PORT = 65432  # Port number on which the server is listening. Must match the server port.
SERVER_ADDRESS = '127.0.0.1'  # The address of the server. '127.0.0.1' refers to the local machine.

def main():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect the socket to the server address and port
        s.connect((SERVER_ADDRESS, PORT))
        
        while True:
            # Prompt the user to choose an operation
            print("Choose an operation:")
            print("1. Convert string to base64")
            print("2. Convert string to uppercase")
            
            # Get user choice and strip any leading/trailing whitespace
            choice = input("Enter choice (1/2): ").strip()

            # Determine the command based on user choice
            if choice == '1':
                command = 'BASE64'
            elif choice == '2':
                command = 'UPPERCASE'
            else:
                # Inform the user of invalid choice and exit the loop
                print("Invalid choice. Run program again.")
                break

            # Get the string input from the user
            payload = input("Enter the string: ").strip()
            
            # Create the request string with command and payload
            request = f"{command} {payload}"
            
            # Send the request to the server
            s.sendall(request.encode())
            
            # Receive the server's response
            response = s.recv(1024).decode()
            
            # Display the server's response
            print(f"Server response: {response}")

# Execute the main function if this script is run directly
if __name__ == '__main__':
    main()

