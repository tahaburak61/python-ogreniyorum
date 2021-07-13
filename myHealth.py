alis = int(input("arabanın alış fiyatı")) 
satis = int(input("arabanın satış fiyatı"))

karlilik = satis - alis

if(karlilik == 0):
    print("bu araba satışından kar etmediniz")
elif(karlilik > 0):
    print("bu araba sattışından kar ettiniz")
else:
    print("bu araba satışından kar edemediniz zarar ettiniz")
