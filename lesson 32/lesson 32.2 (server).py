def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message


import socket

HOST = '127.0.0.1'
PORT = 12345

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Ехо-сервер запущено на {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"З'єднання встановлено: {client_address}")

            key = int(client_socket.recv(1024).decode())

            data = client_socket.recv(1024).decode()

            encrypted_data = caesar_encrypt(data, key)

            client_socket.sendall(encrypted_data.encode())

            print("Дані успішно оброблені та відправлені назад клієнту.")

            client_socket.close()

if __name__ == '__main__':
    run_server()
