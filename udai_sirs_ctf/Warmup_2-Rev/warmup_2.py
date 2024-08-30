from random import randint
from secret import flag
from friends_wordlist import x

words1 = []
words2 = []
for i in x:
	if len(i) < 6:
		words1.append(i[-1:])
		words2.append(i[1:2])

out = ""
for i in range(len(flag)):
	if i%2 == 0:
		out+=chr(ord(flag[i])^ord(words1[i]))
	else:
		out+= chr(ord(flag[i]) ^ ord(words2[i]))
f = open("output.txt","w")
f.write(out)
