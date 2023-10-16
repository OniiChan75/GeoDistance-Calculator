import socket
import threading
import math


def distanceCalc(lat1, lon1, lat2, lon2):
    # Calculate the distance between the two coordinates using the Haversine formula
    R = 6371  # Radius of the earth in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance


def handle_client(client_socket):
    try:
        # Get the client's address and port
        client_address, client_port = client_socket.getpeername()
        print(f"Client connected from {client_address}:{client_port}")

        # Receive the latitude and longitude coordinates from the client
        received_data = client_socket.recv(1024).decode()
        coordinates = received_data.split(";")

        if len(coordinates) != 2:
            print("Invalid packet:", received_data)
        else:
            coordinates1 = coordinates[0].split(",")
            lat1, lon1 = map(float, coordinates1)
            coordinates2 = coordinates[1].split(",")
            lat2, lon2 = map(float, coordinates2)

        distance = distanceCalc(lat1, lon1, lat2, lon2)
        client_socket.send(str(distance).encode())
    except Exception as e:
        print(f"Error while handling client from {client_address}:{client_port}: {e}")
    finally:
        client_socket.close()


def start_server(host, port):
    # Create a server socket object and bind it to the host and port number
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Listen for incoming connections and spawn a new thread to handle each client that connects
    server_socket.listen()
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == '__main__':
    # Call the start_server function with the desired host and port number
    start_server('', 8000)
