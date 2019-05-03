def pangkat(x,y):
    i = 1
    pkt = 1
    while i <= y:
        i += 1
        pkt = pkt * x

    return pkt

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))