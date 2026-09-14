a = int(input("sayı biri giriniz"))
b = int(input("sayı ikiyi giriniz"))
c = input ("hangi işlem?")

def topla(a, b):
    return(a + b)
    
def çıkar(a, b):
    return(a - b)

def böl(a, b):
    return(a / b)

def çarp(a, b):
    return(a * b)

if c == "+":
    sonuç = topla(a, b)
elif c == "-":
    sonuç = çıkar(a, b)
elif c == "/":
    sonuç = böl(a, b)
elif c == "*":
    sonuç = çarp(a, b)
print("sonuç =", sonuç)