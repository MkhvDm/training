import math

angle_list = [i for i in range(0,50,5)]

print(angle_list)

D = 100 # sm

AB_list = []

for angle in angle_list:
    print(angle)
    angle_rad = math.radians(angle)
    print('Angle (rad) =', angle_rad)
    tan_a = math.tan(angle_rad)
    print('tan(a) =', tan_a)
    b = tan_a * D
    print('b =', b)
    print()
    AB_list.append((angle, round(b, 3)))

print(AB_list)

with open('Good angle.txt', 'w') as text_file:
    for string in AB_list:
        text_file.write(str(string)+'\n')