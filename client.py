import socket

port = 5050
server_ip = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server_ip,port))

def send_message(msg):

    # encoding to utf
    message = msg.encode("utf-8")
    message_length = len(message)

    # setting send_length
    send_length = str(message_length).encode("utf-8")
    send_length += b' ' * (64 - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode("utf-8"))

# these should show up in the server terminal
send_message("hello1") 
send_message("hello2")
send_message("hello2")

# disconnecting
send_message("DISCONNECTED")