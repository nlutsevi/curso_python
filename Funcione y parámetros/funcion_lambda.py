"""
def area_rect(base, altura):
    return base * altura

def area_tri(b, a):
    rec = area_rect(b, a)
    return rec / 2
"""
area_rect = lambda base, altura : base * altura
area_tri = lambda b, a : area_rect(b,a) / 2

mibase = 5
mialtura = 3
print("El área del cuadrado es: ")
print(area_rect(mibase, mialtura))
print("El area del triangulo es: ")
print(area_tri(mibase, mialtura))
