
--------------NOTES--------------

for i in array:
	print(array[i])
---------------------------------
def square(n):
	try:
		return n*n
	except:
		print('You entered zero')	

print(square(4))
---------------------------------
Raw String: r'r tag ignores \t backslash'
---------------------------------
RegEx:


import re #Built in regex package
haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

>>> mo2 = haRegex.search('Ha')
>>> mo2 == None


