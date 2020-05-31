c=[31,2,4,19,23,13,19,18,24,31,22,44,29,9,18,55,9,10,2,37,10,6,23,14,2,20,110,86,82,90,86,83,74]
s="qwertyuiopasdfghjklzxcvbnm1234567890"
m=0
for i in c:
	print(chr(i^ord(s[m])),end='')
	m=m+1
