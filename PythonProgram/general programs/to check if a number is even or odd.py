num = input('enter the number:-  ')
print(type(int(num)))

if int(num)<0:
    raise ValueError('only integer allowed')
if int(num) % 2 == 0:
    print(num,' is even number')
else:
    print(num, 'is odd number')
