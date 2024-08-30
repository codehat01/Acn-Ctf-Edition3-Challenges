cipher_text = "55CGPAIQGP5DP6545C33D5NFXMZDYYV5NXFCMXZN&&PVPDXFFPTKDTKVZRYTHFLF"
key = "REDACTED"
flag = "REDACTED"

key_padded = ""

def pad(x,y):
	padded = ""
	while (len(padded) <= len(y)):
		for i in x:
			padded += i
	return padded
key_padded = pad(key,flag)
xored_output = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(flag,key))
f = open("out.txt", 'w')
f.write(xored_output)



