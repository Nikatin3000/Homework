import multiprocessing
import socket

def connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr}")
        process = multiprocessing.Process(target=connection, args=(conn,))
        process.start()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1234

    start_server(host, port)
