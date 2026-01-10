import socket
import threading

class DistributedServer:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port 
        self.clients = {} #client_id: for connection
        self.client_counter = 0
        self.lock = threading.Lock()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        print(f"Server started on {self.host}:{self.port}")
        print("Waiting for clients to connect...")

        while True:
            conn, addr = server.accept()
            print(f"\nNew connection from {addr}")

            with self.lock:
                self.client_counter += 1
                client_id = self.client_counter
                self.clients[client_id] = conn
    
            conn.send(f"Welcome! You are client #{client_id}\n".encode())

            thread = threading.Thread(target= self.handle_client, args=(client_id, conn))
            thread.start()

    def handle_client(self, client_id, conn):    #Handle message from a specific client
        print(f"Client #{client_id} connected. Total clients: {len(self.clients)}")

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                message = data.strip()
                print(f"Client #{client_id}: {message}")

                #Broadcast to all other clients
                self.broadcast(f"Client #{client_id} says: {message}", exclude = client_id)
        except Exception as e:
            print(f"Error with client #{client_id}: {e}")
        finally:
            self.disconnect_client(client_id, conn)
        
    def broadcast(self, message, exclude=None):
        with self.lock:
            clients_snapshot = list(self.clients.items())

        for cid, conn in clients_snapshot:
            if cid != exclude:
                try:
                    conn.send(f"{message}\n".encode())
                except:  # noqa: E722
                    pass

    def disconnect_client(self, client_id, conn):
        with self.lock:
            if client_id in self.clients:
                del self.clients[client_id]
        conn.close()
        print(f"Client #{client_id} disconnected. Total clients: {len(self.clients)}")

if __name__ == "__main__":
    server = DistributedServer()
    server.start()

    

            
