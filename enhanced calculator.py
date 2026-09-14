while True:
    try:
        a = int(input("Sayı biri giriniz"))
        break
    except ValueError:
        print("Hatalı giriş")
while True:
    işlem = input("işlemi giriniz")
    if işlem in["+", "-", "*", "/","^", "√"]:
        break
while True:
    try:
        b = int(input("Sayı ikiyi giriniz"))
        break
    except ValueError:
        print("Hatalı giriş")


def topla(a, b):
    return(a + b)
    
def çıkar(a, b):
    return(a - b)

def böl(a, b):
    return(a / b)

def çarp(a, b):
    return(a * b)

def kök(a, b):
    return(a**(1/b))

def üs(a, b):
    return(a**b)

sonuç ={
    "+":topla,
    "-":çıkar,
    "*":çarp,
    "/":böl,
    "^":üs,
    "√":kök
}
print("sonuç =", sonuç[işlem](a, b))