class player():
    hp = 0
    ad = 0
    invntory = []

    def __init__(self, hp, ad, invntory):
        self.hp = hp 
        self.ad = ad 
        self.invntory = invntory

start = True

while start:
    print("Spiel starten")

    menu_chose = input(">")

    if menu_chose == "Spiel starten":
        pass 
    else:
        print("Menüpunkt exestiert nicht.")