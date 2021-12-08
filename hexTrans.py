#!/usr/bin/python3
import sys

if len(sys.argv) != 3:
    print('''Usage: hexTrans <hexString> <Separator>

Example: 
        input: hexTrans 'aabbcc' '%'
        output: %aa%bb%cc
    ''')
    exit()

hex = sys.argv[1]
sig = sys.argv[2]

if len(hex)%2 != 0:
    print("Please enter an even number!")
    exit()

slices = [hex[i:i+2] for i in range(0, len(hex), 2)]

ans = sig + sig.join(slices)

print(ans)
