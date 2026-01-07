# Distributed Clients - Multi-Client Chat Server

A Python-based distributed client-server system demonstrating concurrent connections, threading, and real-time message broadcasting.

## 📖 Overview

This project implements a distributed client-server architecture where multiple clients can connect to a central server and communicate in real-time. The server manages concurrent connections through threading, ensuring each client receives messages from all other clients while maintaining thread-safe operations.

Built from scratch to demonstrate understanding of distributed systems concepts applicable to robotics and multi-agent systems.

## Features

- **Multi-client support** - Handle unlimited simultaneous client connections
- **Real-time broadcasting** - Messages instantly sent to all connected clients
- **Thread-safe operations** - Uses locks to prevent race conditions
- **Graceful disconnection** - Clients can connect and disconnect cleanly without affecting others
- **Unique client IDs** - Each client receives a unique identifier
- **Robust error handling** - Handles network issues and unexpected disconnections
- **No external dependencies** - Uses only Python standard library

##  Technologies Used

- **Python 3.x**
- `socket` - TCP/IP networking and communication
- `threading` - Concurrent client handling and multi-threading
- `threading.Lock()` - Thread synchronization for safe data access

## Requirements

- Python 3.6 or higher
- No external libraries required (uses built-in modules only)

## Installation & Setup

### Clone the Repository
```bash
