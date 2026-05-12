import json
from datetime import date
import os

filnamn = "person.json"

# Läs in personer från JSON-filen
if os.path.exists(filnamn):
    with open(filnamn, "r", encoding="utf-8") as fil:
        personer = json.load(fil)
else:
    personer = []

while True:

    print("\nSkriv 'exit' för att avsluta")
    print("Skriv 'sammanställ' för att visa alla personer")
    print("Skriv annars ett nytt förnamn\n")

    first_name = input("Förnamn: ").strip().title()

    # Avsluta programmet
    if first_name.lower() == "exit":
        print("\nProgrammet avslutas.")
        break

    # Visa sammanställning
    if first_name.lower() == "sammanställ":

        if len(personer) == 0:
            print("\nInga personer sparade.")
        else:
            # Sorterar efter minst dagar kvar
            sorterade = sorted(personer, key=lambda x: x["dagar_kvar_till_100"])

            print("\n--- Sammanställning ---")

            for person in sorterade:
                print(
                    person["förnamn"],
                    person["efternamn"],
                    "-",
                    person["dagar_kvar_till_100"],
                    "dagar kvar till 100 år"
                )

        continue

    last_name = input("Efternamn: ").strip().title()

    # Kontrollera om personen redan finns
    person_hittad = False

    for person in personer:
        if (
            person["förnamn"].lower() == first_name.lower()
            and person["efternamn"].lower() == last_name.lower()
        ):

            print("\nPersonen finns redan sparad!")
            print("Namn:", person["förnamn"], person["efternamn"])
            print("Födelsedatum:", person["födelsedatum"])
            print("Dagar kvar till 100 år:", person["dagar_kvar_till_100"])

            person_hittad = True
            break

    if person_hittad:
        continue

    # Felhantering för datum
    while True:
        try:
            print("\nSkriv födelsedatum")
            print("Exempel:")
            print("År: 1991")
            print("Månad: 02")
            print("Dag: 12")

            year = int(input("Födelseår: "))
            month = int(input("Födelsemånad: "))
            day = int(input("Födelsedag: "))

            # Kontrollerar att datumet finns
            fodelsedatum = date(year, month, day)

            break

        except ValueError:
            print("\nFelaktigt datum!")
            print("Försök igen.\n")

    # Räknar ut 100-årsdagen
    hundra_ars_dag = date(year + 100, month, day)

    to_day = date.today()

    skillnad = hundra_ars_dag - to_day

    # Skapar person
    new_person = {
        "förnamn": first_name,
        "efternamn": last_name,
        "födelsedatum": str(fodelsedatum),
        "dagar_kvar_till_100": skillnad.days
    }

    # Lägg till personen
    personer.append(new_person)

    # Sparar till JSON-fil
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(personer, fil, ensure_ascii=False, indent=4)

    print("\nNy person sparad!")
    print("Det är", skillnad.days, "dagar kvar tills personen fyller 100 år.")