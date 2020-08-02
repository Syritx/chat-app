import socket
import threading

port = 5050
server_ip = socket.gethostbyname(socket.gethostname())

# starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip,port))

def client_handling(client,address):
    print(f"connection from {address}")

    is_client_connected = True

    while is_client_connected:
        message_length = client.recv(64).decode("utf-8")

        if message_length != None: # checking if the message length (or message) isn't None
            message_length = int(message_length)
            message = client.recv(message_length).decode("utf-8")

            # checking if the message is the disconnect message
            if message == "DISCONNECTED":
                print(f"IP: {address}: DISCONNECTED FROM THE SERVER")
                is_client_connected = False
                break
            # if not then print the message
            else:
                print(f"IP: {address}: {message}")
                client.send("message seen".encode("utf-8"))

    client.close()

def start():
    server.listen(10)
    while True:
        client, addr = server.accept() # accepting a new client

        # making a new thread
        thread = threading.Thread(target=client_handling, args=(client,addr))
        thread.start()
        print(f"CLIENTS: {threading.activeCount()-1}")


start()