import socket

def check_port(port):
    host = "127.0.0.1"  # Check this computer only

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on localhost.")
        else:
            print(f"Port {port} is CLOSED on localhost.")

    except socket.error as error:
        print("Unable to check port:", error)


try:
    port = int(input("Enter a port number (1-65535): "))

    if 1 <= port <= 65535:
        check_port(port)
    else:
        print("Invalid port. Enter a number from 1 to 65535.")

except ValueError:
    print("Invalid input. Please enter a whole number.")
