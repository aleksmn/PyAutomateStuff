# List Methods

spam = ['a', 'b', 'c']
spam.index('b') # 1
spam.append('z') # ['a', 'b', 'c', 'z']
spam.insert(2, 'hello!') # ['a', 'b', 'hello!', 'c', 'z']
spam.remove('hello!') # ['a', 'b', 'c', 'z']
del spam[0] # ['b', 'c', 'z']
spam.sort(reverse = True) # ['z', 'c', 'b']
spam += ('A', 'B', 'W', 'Z') # ['z', 'c', 'b', 'A', 'B', 'W', 'Z']
spam.sort() # ['A', 'B', 'W', 'Z', 'b', 'c', 'z'
spam.sort(key=str.lower) # ['A', 'B', 'b', 'c', 'W', 'Z', 'z']

print(spam) 
