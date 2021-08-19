def isiklar(isik):
    if(isik == "kirmizi"):
        return "dur"
    elif(isik == "sari"):
        return "hazirda bekle"
    elif(isik == "yesil"):
        return "gec"
    else:
        return "yanlis girdi"

print(isiklar("sari"))
print(isiklar("yesil"))
print(isiklar("kirmizi"))
print(isiklar("yesil"))