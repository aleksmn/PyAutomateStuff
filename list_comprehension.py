temps = [221, 234, 340, -9999, 230]

def new_temps(temps):
    return[temp / 10 for temp in temps if temp != -9999]

def new_temps2(temps):
    return[temp / 10 if temp != -9999 else 0 for temp in temps]

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]

def get_sum(lst):
    return sum([float(i) for i in lst])


print(get_sum(['1.3', '1.5', 8]))



