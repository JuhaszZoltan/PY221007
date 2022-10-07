f = float(input('mennyi az autó 100 Km-enkénti fogyasztása? '))
s = float(input('hány Km a megtett út? '))
p = int(input('mennyibe kerül egy liter benizin? '))
n = int(input('hány utas van? '))

teljes_koltseg = s * p * f / 100

print(f'Egy főre jutó útiköltség: {round(teljes_koltseg / n)} HUF')