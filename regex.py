import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group() # '415-555-4242'
mo.group(1) # '415'

#batRegex = re.compile(r'Bat(wo)?man') # ? once or zero
#batRegex = re.compile(r'Bat(wo)*man') # * zero or more
batRegex = re.compile(r'Bat(wo)+man') # + once or more
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('My numbers are 415-555-4242, 111-222-3467, 333-555-7232.')
print(mo)


beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there!') # <re.Match object; span=(0, 5), match='Hello'>

allDigitsRegex = re.compile(r'^\d+$')
allDigitsRegex.search('1242353456') #<re.Match object; span=(0, 10), match='1242353456'>


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name = nameRegex.findall('First Name: Mikhail Last Name: Aleksandrov')
