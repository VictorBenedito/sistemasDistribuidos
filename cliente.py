import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.sendall(b"Olá, servidor!")
data = client.recv(1024)
print("Resposta do servidor:", data.decode())
client.close()
