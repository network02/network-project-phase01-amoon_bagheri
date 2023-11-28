from typing import List
import os
import sys
import socket


def check_host_status_ports_and_services(ip_address: str, ports: List[str]):
    ret = os.system(f"ping -c 1 {ip_address}")
    if ret == 0:
        print(f"{ip_address} is online")
        protocol_name = 'tcp'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in ports:
            location = (ip_address, int(port))
            result = sock.connect_ex(location)

            if result == 0:
                service_name = socket.getservbyport(int(port), protocol_name)
                print(f"open port detected: {ip_address}    -- Port: {port}  -- Service: {service_name}")


args = sys.argv
if len(args) > 2:
    check_host_status_ports_and_services(args[1], args[2:])
