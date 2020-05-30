import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # [1, 2, 3, 'Hello']


spam = ['A', 'B', 'C']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese) # ['A', 42, 'C']
print(spam) # ['A', 'B', 'C']
