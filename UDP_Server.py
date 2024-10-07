import socket

# Initialize a list to keep track of checked-in students
checked_in_students = []

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address and port
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)

    print("Socket created and bound")
    print("Listening for messages...\n")

    while True:
        try:
            # Receive the message from the client
            client_message, client_address = sock.recvfrom(2000)
            message = client_message.decode()
            print(f"Received message from IP: {client_address[0]} and Port No: {client_address[1]}")
            print(f"Client Message: {message}")

            response_message = process_message(message)
            sock.sendto(response_message.encode(), client_address)

            # Print current checked-in students
            print("Current Checked-In Students:", checked_in_students)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Closing the socket
    sock.close()

def process_message(message):
    global checked_in_students

    parts = message.split('-')
    
    if len(parts) != 3:
        return "Invalid message format."

    roll_number = parts[1]
    action = parts[2]

    if action == "CI":  # Check in
        if roll_number in checked_in_students:
            return "You are already here."
        else:
            checked_in_students.append(roll_number)
            return f"Welcome Student {roll_number}"

    elif action == "CO":  # Check out
        if roll_number not in checked_in_students:
            return "You didn’t check in today. Contact System Administrator."
        else:
            checked_in_students.remove(roll_number)
            return f"Goodbye Student {roll_number}! Have a nice day."

    return "Invalid action."

if __name__ == "__main__":
    main()