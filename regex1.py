import re

phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d\-\d\d\d\d')

message = 'Call me at 415-555-1011 tomorrow'



mo = phoneNumRegex.search(message)
print(mo.group())

#re.compile(), matched_object = re.search(), matched_object.group()


