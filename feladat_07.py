a = int(input('egyik befogó hossza (cm): '))
b = int(input('másik befogó hossza (cm): '))

if a <= 0 or b <= 0:
    print('nem létezik ilyen háromszög')
else:
    print(f'a háromszög átfogója: {(a ** 2 + b ** 2) ** .5} cm')