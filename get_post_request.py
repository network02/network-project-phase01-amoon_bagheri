import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        user_input = input("Enter 'GET user_id' or 'POST user_name user_age' to simulate a request: ")
        if user_input[:3] == "GET" or user_input[:4] == "POST":
            s.sendall(user_input.encode())
            data = s.recv(1024)
            print(data.decode())
        else:
            print('invalid command')
