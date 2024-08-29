def xor(s1, s2):
    res = [0] * 8  
    for i in range(len(res)):
        q = s1[i]
        d = s2[i]
        k = q ^ d
        res[i] = k
    res = bytes(res) 
    return res

def add_pad(msg):
    l = 8 - len(msg) % 8
    msg += bytes([l] * l)  
    return msg

with open('flag.png', 'rb') as f:
    data = f.read()
    

data = add_pad(data)

with open('key.txt', 'rb') as f:
    key = f.read()
    print(key)

enc_data = b''  
for i in range(0, len(data), 8):
    enc = xor(data[i:i+8], key)
    enc_data += enc

with open('encrypted.png', 'wb') as f:
    print(enc_data)
    f.write(enc_data)
