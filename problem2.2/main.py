bilangan = int(input())
for i in reversed(range(1,bilangan+1)):
    if bilangan % i == 0:
        print(i)
        i += 1