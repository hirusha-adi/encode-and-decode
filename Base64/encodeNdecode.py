import base64
import os

def encode():
    os.system('cls')
    print(""" 
 __     __ __  __  __ 
|_ |\ |/  /  \|  \|_
|__| \|\__\__/|__/|__
    """)
    s = input("\nencode>> ")
    # Encoding the string into bytes
    b = s.encode("UTF-8")
    # Base64 Encode the bytes
    e = base64.b64encode(b)
    print(e)

def decode():
    os.system('cls')
    print(""" 
 __  __ __ __  __  __ 
|  \|_ /  /  \|  \|_  
|__/|__\__\__/|__/|__ 
    """)
    e = input("\ndecode>> ")
    # Encoding the Base64 encoded string into bytes
    b1 = e.encode("UTF-8")
    # Decoding the Base64 bytes
    d = base64.b64decode(b1)
    # Decoding the bytes to string
    s2 = d.decode("UTF-8")
    print(s2)

os.system('cls')
print(""" 
 ███████████                              ████████  █████ █████ 
░░███░░░░░███                            ███░░░░███░░███ ░░███  
 ░███    ░███  ██████    █████   ██████ ░███   ░░░  ░███  ░███ █
 ░██████████  ░░░░░███  ███░░   ███░░███░█████████  ░███████████
 ░███░░░░░███  ███████ ░░█████ ░███████ ░███░░░░███ ░░░░░░░███░█
 ░███    ░███ ███░░███  ░░░░███░███░░░  ░███   ░███       ░███░ 
 ███████████ ░░████████ ██████ ░░██████ ░░████████        █████ 
░░░░░░░░░░░   ░░░░░░░░ ░░░░░░   ░░░░░░   ░░░░░░░░        ░░░░░  
                                                                
                    Encoder and Decoder
                      by ZeaCeR#5641
               Press 1 to Encode, 2 to Decode
""")

DorE = input("\noption>> ")

try:
    if DorE == '1':
        encode()
    elif DorE == '2':
        decode()
    else:
        print("[-] Please enter a valid option! ")
except Exception as e:
    print("error: ", e)
except(KeyboardInterrupt, SystemExit):
    print("Exitting program! bye bye!")