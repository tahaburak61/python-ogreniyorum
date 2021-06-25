def hesapla(al, sat):
    oran = int(((sat - al) / al) * 100)
    cevap = ""
    if oran == 0: cevap = "Bu araba satın alma fiyatından sattınız."
    if oran < 0: cevap = "Bu araba satışında {} kadar zarar ettiniz. ({}%)"
    if oran > 0: cevap = "Bu araba satışında {} kadar kâr ettiniz. ({}%)"
    print(cevap.format(abs(sat - al), abs(oran)))


def main():
    alis = int(input("Alış fiyatı: "))
    satis = int(input("Satış fiyatı: "))
    hesapla(alis, satis)


main()