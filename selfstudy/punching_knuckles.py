def func(example):
    example.sort()
    if (example[0] ** 2) + (example[1] ** 2) == example[2] ** 2:
        return True
    else:
        return False
        
        
test = [100, 3, 65]

print(func(test))