import socket
import threading

class DistributedClient:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):      #Connect to the server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")

            thread = threading.Thread(target=self.receive_messages)
            thread.daemon = True
            thread.start()

            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def receive_messages(self):  #Receive messages from the server
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if message:
                    print(f"\n{message.strip()}")
                    print("You:", end=' ', flush=True)
                else:
                    break
            except:
                break
        print(f"\nDisconnected from server.")

    def send_message(self, message):  #Send message to the server
        try:
            self.socket.send(message.encode())
        except Exception as e:
            print(f"Failed to send message: {e}")

    def run(self):
        if not self.connect():
            return
        print("\nType your message and press Enter to send.")
        print("type 'quit' to exit. \n")

        while True:
            try:
                message = input("You:")
                if message.lower() == 'quit':
                    break
                self.send_message(message)
            except KeyboardInterrupt:
                break

        self.socket.close()
        print("Goodbye!")

if __name__ == "__main__":
    client = DistributedClient()
    client.run()



