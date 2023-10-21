import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostbyname("192.168.5.117")#poner acá localhost
port=5150

client.connect((host,port))
data=client.recv(1024)
print(bytes.decode(data))
while True:
    message=input("Cliente (Tu) dice: ")
    client.send(str.encode(message))
    if message.lower()=="exit":
        break
    data=client.recv(1024)
    print("Servidor dice: ", bytes.decode(data))
    if message.lower()=="exit":
        break
print("saliendo..")
client.close()