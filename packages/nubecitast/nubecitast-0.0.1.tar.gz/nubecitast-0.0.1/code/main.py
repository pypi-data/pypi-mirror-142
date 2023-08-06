# Libreria desarrollada por Sebastian Tobar Quintero
# Última modiciación 3/03/2022

import socket
import sys

# Parametros
ip = '127.0.0.1'
port = 476 # Puerto por defecto de admin_container
           # 476 - 490 Unofficial Centro Software ERP ports

def set_ip(new_ip):
    global ip

    ip = new_ip

def set_port(new_port):
    global port

    port = new_port

def connect_socket():
    global ip, port

    return socket.create_connection((ip, port))

# Retorna si la operacion fue exitosa o no
def create_container(sock, name):
    try:
        order = "-c"
        message = str.encode(order + name)
        sock.sendall(message)

        amount_received = 0
        amount_expected = 2

        while amount_received < amount_expected:
            data = sock.recv(512)
            amount_received += len(data)
    except:
        return False
    finally:
        if(int(data[2])):
            return True
        else:
            return False

# Retorna la lista de contenedores guardada en el admin_container
def list_containers(sock):
    try:
        order = "-l"
        message = str.encode(order)
        sock.sendall(message)

        amount_received = 0
        amount_expected = 2

        while amount_received < amount_expected:
            data = sock.recv(512)
            amount_received += len(data)
    except Exception as e:
        return "error" + str(e)
    finally:
        return data.decode("utf-8")

# Retorna si el contenedor se detuvo o no
def stop_container(sock, id):
    try:
        order = "-s"
        message = str.encode(order  + id)
        sock.sendall(message)

        amount_received = 0
        amount_expected = 2

        while amount_received < amount_expected:
            data = sock.recv(512)
            amount_received += len(data)
    except:
        return False
    finally:
        if(int(data[2])):
            return True
        else:
            return False

# Retorna si el contenedor fue borrado o no
def delete_container(sock, id):
    try:
        order = "-d"
        message = str.encode(order + id)
        sock.sendall(message)

        amount_received = 0
        amount_expected = 2

        while amount_received < amount_expected:
            data = sock.recv(512)
            amount_received += len(data)
    except:
        return False
    finally:
        if(int(data[2])):
            return True
        else:
            return False

def close_connection(sock):
    sock.close()
