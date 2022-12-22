import math
for i in range (0,23,1):
    sinevalue=(math.sin(math.radians(15*i)))
    cosvalue=(math.cos(math.radians(15*i)))
    roundoff1=round(sinevalue,4)
    roundoff2=round(cosvalue,4)
    print(roundoff1,roundoff2)


