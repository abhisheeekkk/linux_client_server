#Author : Abhishek
#Mail : abhishekshukla9586@gmail.com


import socket

# Configuration
PORT = 65432  # Must match server port
SERVER_ADDRESS = '127.0.0.1'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS, PORT))
        while True:
            print("Choose an operation:")
            print("1. Convert string to base64")
            print("2. Convert string to uppercase")
            choice = input("Enter choice (1/2): ").strip()

            if choice == '1':
                command = 'BASE64'
            elif choice == '2':
                command = 'UPPERCASE'
            else:
                print("Invalid choice. Run program again.")
                break

            payload = input("Enter the string: ").strip()
            request = f"{command} {payload}"
            s.sendall(request.encode())
            response = s.recv(1024).decode()
            print(f"Server response: {response}")

if __name__ == '__main__':
    main()

