# В списке x = [4,6,0,0,1,2,3,0,0,0,50] найти кол-во нулей
x = [4,6,0,0,1,2,3,0,0,0,50]

zeros = 0

for i in x:
    if i == 0:
        zeros += 1
print(f"У вас {zeros} нулей в списке {x}")