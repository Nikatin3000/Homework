def caesar_decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message


import socket

HOST = '127.0.0.1'
PORT = 12345

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        key = int(input("Введіть ключ для шифрування: "))

        client_socket.sendall(str(key).encode())

        data = input("Введіть дані для відправлення: ")

        client_socket.sendall(data.encode())

        encrypted_data = client_socket.recv(1024).decode()

        decrypted_data = caesar_decrypt(encrypted_data, key)

        print("Зашифровані дані: ", encrypted_data)
        print("Розшифровані дані: ", decrypted_data)

if __name__ == '__main__':
    run_client()
