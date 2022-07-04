def mile2km():
    miles=float(input("Miles: "))
    con_ratio=1.60934
    km=con_ratio*miles
    print(miles,"Miles=",km,"Km")
    return km
mile2km()

def km2mile():
    km=float(input("Km:"))
    con_ratio=0.6213727291494633
    miles=con_ratio*km
    print(km,"Km=",miles,"Miles")
    return miles
km2mile()


