

ukoly = []
def hlavni_menu():
    vyber1 = "1. Přidat nový úkol"
    vyber2 = "2. Zobrazit všechny úkoly"
    vyber3 = "3. Odstranit úkol"
    vyber4 = "4. Konec programu"
    print("Správce úkolů - Hlavní menu")
    print(vyber1)
    print(vyber2)
    print(vyber3)
    print(vyber4)
    while True:
        zvoleno = input("Vyberte možnost (1-4): ")
        print()
        if not zvoleno.isdigit():
            print("Neplatná volba - Zadejte číslo")
            continue
        zvoleno = int(zvoleno)
        if  zvoleno < 1 or zvoleno > 4:
            print("Neplatná volba - Zadejte číslo 1-4")
            continue
        return zvoleno

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        if len(nazev) == 0:
            print("Nezadali jste název úkolu")
        else:
            break
    while True:
        popis = input("Zadejte popis úkolu: ")
        if len(popis) == 0:
            print("Nezadali jste popis úkolu")
        else:
            break
    ukoly.append((nazev, popis))
    print(f"Úkol '{nazev}' byl přidán.")
    print()
    

def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Žádné úkoly.")
        print()
        return
    for i, (nazev, popis) in enumerate(ukoly, start=1):
        print("Seznam úkolů:")
        print(f"{i}. {nazev} - {popis}")
        print()
    

def odstranit_ukol():
    if not ukoly:
        print("Žádné úkoly k odstranění")
        print()
        return
    zobrazit_ukoly()
    while True:
        vyber = input("Zadejte číslo úkolu, který chcete odstranit: ")
        if not vyber.isdigit():
            print("Zadejte číslo")
            continue
        if int(vyber) < 1 or int(vyber) > len(ukoly):
            print("Neplatné číslo úkolu")
            continue
        smazane = ukoly.pop(int(vyber)-1)
        print(f"Úkol '{smazane[0]}' byl odstraněn.")
        print()
        break

def hlavni_program():
    while True:
        volba = hlavni_menu()
        if volba == 1:
            pridat_ukol()
        elif volba == 2:
            zobrazit_ukoly()
        elif volba == 3:
            odstranit_ukol()
        elif volba == 4:
            print("Program ukončen.")
            break
    
if __name__ == "__main__":
    hlavni_program()






