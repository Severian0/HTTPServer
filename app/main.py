import socket


def main():
    print('1')
    server_socket = socket.create_server(("localhost", 4221))
    client_socket, _ = server_socket.accept()
    request = client_socket.recv(4096)
    lines = request.decode().split("\r\n")
    method, path, version = lines[0].split(" ")
    if path == "/":
        client_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")
    elif '/echo/' in str(path):
        message = path.split('/echo/')[-1]
        response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(message)}\r\n\r\n{message}'
        client_socket.send(response.encode())
    elif str(path) == '/user-agent':
        message = lines[2].split(" ")[1]
        response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(message)}\r\n\r\n{message}'
        client_socket.send(response.encode())
    else:
        client_socket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
