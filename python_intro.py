print("terena")
if 3>2:
    print("dziala")
if 3>2:
    print("jest jednak wieksze")
else:
    print("5nie jest wieksze od 2")
name = "Sonja"
if name =="Ola":
    print("hej Ola")
elif name =="Sonja":
    print("hej Sonja")
else:
    print("hej nieznajoma!")
def hej():
    print("hej!")
    print("jak sie masz")
hej()
def hej(imie):
    if imie == "Ola":
        print("hej ola")
    elif imie =="sonja":
        print("hej sonja!")
    else:
        print("hej nieznajoma!")
hej("ola")
def hej(imie):
    print("hej" + "!")
hej("rachel")
dziewczyny = ["rachela","monika","eliza","margaret"]
def hej(imie):
    print("hej" + imie + "!")
dziewczyny = ["rachela","monika","eliza","margaret"]
for imie in dziewczyny:
    hej(imie)
    print("kolejna dziewczyna")
for i in range(1,6):
    print(i)
