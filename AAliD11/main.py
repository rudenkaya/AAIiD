import math

def punkt_srodkowy(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def kat_nachylenia(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def pole_trojkata(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)

def relacja_prostej_do_okregu(x1, y1, x2, y2, xc, yc, r):
    licznik = abs((y2 - y1)*xc - (x2 - x1)*yc + x2*y1 - y2*x1)
    mianownik = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    odleglosc = licznik / mianownik if mianownik != 0 else float('inf')
    if odleglosc < r:
        return "Przechodzi przez okrąg"
    elif odleglosc == r:
        return "Styka się z okręgiem"
    else:
        return "Nie przecina okręgu"

print("Podaj dane dla punktów (wektor, trójkąt, prosta):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3 (dla trójkąta): "))
y3 = float(input("y3 (dla trójkąta): "))

print("\nPodaj dane dla okręgu:")
xc = float(input("x środka okręgu: "))
yc = float(input("y środka okręgu: "))
r = float(input("promień okręgu: "))


print("\n WYNIKI ")
print("Punkt środkowy:", punkt_srodkowy(x1, y1, x2, y2))
print("Kąt nachylenia wektora:", kat_nachylenia(x1, y1, x2, y2), "stopni")
print("Pole trójkąta:", pole_trojkata(x1, y1, x2, y2, x3, y3))
print("Relacja prostej do okręgu:", relacja_prostej_do_okregu(x1, y1, x2, y2, xc, yc, r))
