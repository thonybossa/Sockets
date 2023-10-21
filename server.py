import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=''
port=5150
server.bind((host,port))
server.listen(5)
print("En espera por cliente...")
client,addr=server.accept()
print("Se acepta cliente desde :",addr)
client.send(str.encode("Hola desde mi servidor"))
while True:
    data=client.recv(1024)
    message=bytes.decode(data)
    print("Cliente dice:", message)
    if message.lower()=="exit":
        break
    response=input("Servidor (Tu) dice: ")
    client.send(str.encode(response))
    if message.lower()=="exit":
        break
print("Cerrando ")
client.send(str.encode("exit"))
client.close()