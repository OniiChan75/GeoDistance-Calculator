# GeoDistance Calculator

GeoDistance Calculator is a Python application that allows clients to send pairs of geographic coordinates (latitude and longitude in decimal) to a server, which then calculates the distance between these coordinates and sends the result back to the client. The server is designed to handle multiple connections using threads.

## Features
- Communicates over TCP sockets.
- Handles multiple client connections concurrently using threads.
- Calculates the distance between geographic coordinates using the Haversine formula.
- Provides a simple client and server implementation.

## Prerequisites
- Python 3.x

## Usage

### Client
1. Clone the repository to your local machine.

2. Navigate to the client directory.

3. Modify the `server_address` and `server_port` in the `client.py` script to match the server's IP address and port.

4. Run the client script:
```bash
python client.py
```
5. Follow the prompts to enter two sets of geographic coordinates (latitude and longitude).

### Server
1. Clone the repository to your local machine.

2. Navigate to the server directory.

3. Modify the `server_port` in the `server.py` script if needed.

4. Run the server script:
```bash
python server.py
```

## Contributing
Contributions are welcome! If you would like to contribute to this project, please open an issue or create a pull request.

## Creators
Project created by Gabriele Meles and Giorgio Tentorio