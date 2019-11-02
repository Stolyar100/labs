"""
the program that calculate start start values of my course work.
task:
get last number of gradebook add to it 12 to have z0 and get second last number of gradebook and add to it 11
after that I need to find  eight more different z and g values using formula:
g_(i) = (z_(i-1) + i)mod16     _(i-1) and _(i) - indexes
z_(i) = (g_(i-1) + 1)mod16
after each step I have to add 1 to i
"""

G = []
Z = []

while 1:
    try:
        last_numbers = int(input('Enter two last numbers of gradebook: '))
        if len(str(last_numbers)) != 2:
            print('ENTER TWO NUMBERS!')
            continue
        elif last_numbers < 0:
            print("ENTER NUMBERS THAT IS MORE THAN 0!")
            continue
        else:
            break
    except ValueError:
        print('ENTER TWO NUMBERS!')

g_now = (int(str(last_numbers)[0]) + 13) % 16
g_last = 0
z_now = (int(str(last_numbers)[1]) + 14) % 16
z_last = 0
x = 0

while 1:
    x += 1

    if g_now not in G and len(G) <= 9:
        G.append(g_now)
    if z_now not in Z and len(Z) <= 9:
        Z.append(z_now)

    g_last = g_now
    z_last = z_now

    g_now = (z_last + x) % 16
    z_now = (g_last + 1) % 16

    if len(G) >= 9 and len(Z) >= 9:
        break

for index, a in enumerate(G):
    binary_a = bin(a).replace('0b', '')
    print(f'g{index} = {a:2} = {a:0>4b}')

print("\n\n")

for index, a in enumerate(Z):
    binary_a = bin(a).replace('0b', '')
    print(f'z{index} = {a:2} = {a:0>4b}')
