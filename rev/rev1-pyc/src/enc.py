from flag import flag
s="qwertyuiopasdfghjklzxcvbnm1234567890"
for x in range(0,len(flag)):
	print(ord(s[x])^ord(flag[x]),end=' ')
#output=31 2 4 19 23 13 19 18 24 31 22 44 29 9 18 55 9 10 2 37 10 6 23 14 2 20 110 86 82 90 86 83 74