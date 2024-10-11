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
    client_message = input("Enter a string: ")

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

    print("After reversing: ", end='')

    # Tokenize the string into words
    words = server_message.split()

    for word in words:
        if all(vowel not in word for vowel in 'aeiouAEIOU'):
            # Reverse the word if it does not contain vowels
            print(word[::-1], end=' ')
        else:
            print(word, end=' ')
    
    print()  # New line after printing all words

    # Clean up and close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
