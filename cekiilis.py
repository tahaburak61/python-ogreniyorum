import random

cekilis = ["Fatih", "Merve", "Ahsen", "Furkan", "Emin", "Mert", "Serkan", "Eda", "Oğuzhan", "Taha", "Mehmet",]

boy = len(cekilis) 

rastgele = random.randint(0, boy-1)

print(cekilis[rastgele])

cekilis.remove(cekilis[rastgele])

print(cekilis)
