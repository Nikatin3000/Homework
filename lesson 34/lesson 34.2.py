import socket
import threading

def new_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(3)
    print("Сервер запущено. Відслідковування підключень...")

    while True:
        client_socket, address = server_socket.accept()
        print("Підключено клієнта за адресою:", address)

        client_thread = threading.Thread(target=new_client, args=(client_socket,))
        client_thread.start()

start_server()