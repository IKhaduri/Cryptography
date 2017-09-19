str1 = input().strip()
a = int(str1,16)
b = int(str(input()).strip(),16)
str = ("%x" % (a^b))
while len(str)<len(str1):
    str = "0"+str
print(str)
