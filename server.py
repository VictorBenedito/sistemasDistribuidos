import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Aguardando conexão...")
conn, addr = server.accept()
print(f"Conectado por {addr}")
data = conn.recv(1024)
print("Recebido:", data.decode())
conn.sendall(b"Mensagem recebida com sucesso!")
conn.close()
