#!/usr/bin/env python3

badchars = input("Enter badchars, example \\x00\\xae\\x24: ")

for i in range(1,256):
  if f'\\x{i:02x}' in badchars: #if the hex char is in badchars, skip it
    continue
  else:
    print(f'\\x{i:02x}',end='') # else print to screen


