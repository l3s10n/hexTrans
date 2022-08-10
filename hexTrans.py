#!/usr/bin/python3
import sys

def hexTrans(hex, sig):
    if len(hex)%2 != 0:
        print("Please enter an even number!")
        exit()

    slices = [hex[i:i+2] for i in range(0, len(hex), 2)]
    ans = sig + sig.join(slices)
    return ans

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print('''Usage: python3 hexTrans.py <hexString> <Separator>

    Example: 
            input: python3 hexTrans.py "aabbcc" "\\x"
            output: \\xaa\\xbb\\xcc
        ''')
        exit()

    hex = sys.argv[1]
    sig = sys.argv[2]

    ans = hexTrans(hex, sig)

    print(ans)
