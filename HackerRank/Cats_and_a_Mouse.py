def catAndMouse(x, y, z):
    AandC = abs(z-x)
    BandC = abs(z-y)
    if AandC > BandC:
        return "Cat B"
    elif BandC > AandC:
        return "Cat A"
    elif BandC == AandC:
        return "Mouse C"


print(catAndMouse(1, 2, 3))  # Cat B
