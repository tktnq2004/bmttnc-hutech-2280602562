import socket
import ssl
import threading

server_address = ('localhost', 12345)
def recieve_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Received from server:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Connection closed by server.")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(server_address)

recieve_thread = threading.Thread(target=recieve_data, args=(ssl_socket,))
recieve_thread.start()

try:
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
    print("Client closed.")