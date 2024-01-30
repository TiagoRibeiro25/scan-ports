import socket

def scan_ports(target_host: str, start_port: int, end_port: int) -> None:
  """
  Scan a range of ports on a target host to check for open ports.
  
  Args:
    target_host: The IP address or hostname of the target host.
    start_port: The starting port number of the range.
    end_port: The ending port number of the range.
  """
  for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((target_host, port))

    if result == 0:
      print(f"Port {port} is open")

    sock.close()

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports(target_host, start_port, end_port)
