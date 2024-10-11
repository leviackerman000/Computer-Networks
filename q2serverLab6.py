import socket

def contains_vowels(word):
    """Check if the word contains any vowels."""
    vowels = "AaEeIiOoUu"
    return any(char in vowels for char in word)

def invert_word(word):
    """Invert the given word."""
    return word[::-1]

def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('', 2000)  # Bind to all interfaces on port 2000
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)
    print("Socket Created and Listening for Incoming Connections.....")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Client Connected with IP: {client_address[0]} and Port No: {client_address[1]}")

        try:
            # Receive the message from the client
            client_message = client_socket.recv(2000).decode()
            if not client_message:
                break
            
            print(f"Client Message: {client_message}")

            # Tokenize the string into words and process them
            words = client_message.split()
            server_message = ""

            for word in words:
                if contains_vowels(word):
                    word = invert_word(word)
                server_message += word + " "

            # Send the modified message back to the client
            client_socket.sendall(server_message.strip().encode())

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Clean up the connection
            client_socket.close()

    # Close the server socket (unreachable in this loop)
    server_socket.close()

if __name__ == "__main__":
    main()
