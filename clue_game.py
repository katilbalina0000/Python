import random

# CASE FILE #001

şüpheliler = ["Alex", "Marcus", "Elena", "Victor"]

katil = random.choice(şüpheliler)

print("===============================")
print("        CASE FILE #001")
print("===============================")
print("\nŞüpheliler:")

for şüpheli in şüpheliler:
    print("-", şüpheli)

print("\nKatil seçildi. Şimdi sıra sende.")

while True:
    tahmin = input("Şüphelini seç: ")

    if tahmin in şüpheliler:
        break

    print("Geçersiz şüpheli.")

if tahmin == katil:
    print("\n✅ CASE CLOSED")
    print("Katil:", katil)
else:
    print("\n❌ Yanlış tahmin.")
    print("Katil:", katil)
