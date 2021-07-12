def modchecker(x, mod=0):
    return lambda y: y % int(x) == mod

mod_3 = modchecker(3)

print(mod_3(3))
print(mod_3(4))

mod_3_1 = modchecker(3,1)

print(mod_3_1(4))
