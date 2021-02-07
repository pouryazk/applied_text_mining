s = "hello pourya"
t = ""
s.strip()
s.rstrip()
s.find(t)
s.rstrip()
s.split('')  # error will be raised, empty character
s.find('o')
s.rfind('o')
s.replace('o', "O")
f = open('UNDHR.txt', 'r')  # read file line by line
f.readline()
f.seek(0)
text = f.read()  # Entire File
text12 = text.splitlines()
# f = open(filename, mode)
f.readline(), f.read(), f.read(n)
for line in f:
	pass
f.seek(0)
# f.write(message)
# f.close()
# f.closed