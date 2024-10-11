import socket

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('127.0.0.1', 2000)

    # Connect to the server
    try:
        client_socket.connect(server_address)
        print("Connected")
    except Exception as e:
        print(f"Connection Failed. Error: {e}")
        return

    # Get input from the user
    client_message = input("Enter Message (Client ID between 0-9): ")

    # Check if the entered message is a valid client ID
    if not client_message.isdigit() or not (0 <= int(client_message) <= 9):
        print("Invalid Client ID. Please enter a number between 0 and 9.")
        client_socket.close()
        return

    # Send the message to the server
    try:
        client_socket.sendall(client_message.encode())
    except Exception as e:
        print(f"Send Failed. Error: {e}")
        return

    # Receive the message back from the server
    try:
        server_message = client_socket.recv(2000).decode()
        print(f"Server Message: {server_message}")
    except Exception as e:
        print(f"Receive Failed. Error: {e}")
        return

    # Clean up and close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
