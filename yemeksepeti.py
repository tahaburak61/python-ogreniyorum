yemekler = ["kıymalı pide", "köfte", "iskender", "hamburger", "döner"]

index = 0

boy = len(yemekler)

print("YEMEKSEPETINE HOSGELDINIZ")

while(index < boy):
    print(index , yemekler[index])
    index = index + 1

secim = int(input("YEMEK SECIN: "))

sepet = []

sepet.append(yemekler[secim])

print("sepetiniz")
print(sepet)