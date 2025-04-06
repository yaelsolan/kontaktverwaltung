# Kontaktverwaltung – Persönliche Version mit Stil ✨
# Mit Update-Funktion, schöner Begrüßung und Struktur

kontakte = {}

# 🎉 Begrüßung
def begruessung():
    print("=" * 42)
    print("  📇 Willkommen im Kontakt-Manager 3000  ")
    print("=" * 42)
    print("Dieses Programm hilft dir, Kontakte zu verwalten.")
    print("Los geht's! \n")

# ➕ Kontakt hinzufügen
def kontakt_hinzufuegen():
    name = input("👤 Name eingeben: ")
    telefon = input("📞 Telefonnummer eingeben: ")
    kontakte[name] = telefon
    print(f"✅ Kontakt '{name}' wurde hinzugefügt.")

# 📋 Kontakte anzeigen
def kontakte_anzeigen():
    if not kontakte:
        print("⚠️ Keine Kontakte vorhanden.")
    else:
        print("\n📋 Deine Kontakte:")
        for name, nummer in kontakte.items():
            print(f"• {name}: {nummer}")
        print()

# 💾 Kontakte speichern
def kontakte_speichern():
    with open("kontakte.txt", "w") as datei:
        for name, nummer in kontakte.items():
            datei.write(f"{name},{nummer}\n")
    print("💾 Kontakte wurden gespeichert.")

# 📂 Kontakte laden
def kontakte_laden():
    try:
        with open("kontakte.txt", "r") as datei:
            for zeile in datei:
                name, nummer = zeile.strip().split(",")
                kontakte[name] = nummer
        print("📂 Kontakte wurden geladen.")
    except FileNotFoundError:
        print("⚠️ Keine gespeicherte Datei gefunden.")

# 🔄 Kontakt aktualisieren
def kontakt_aktualisieren():
    name = input("👤 Welcher Kontakt soll aktualisiert werden? ")
    if name in kontakte:
        neue_nummer = input(f"Neue Nummer für {name}: ")
        kontakte[name] = neue_nummer
        print(f"🔄 Nummer von '{name}' wurde aktualisiert.")
    else:
        print("❌ Kontakt nicht gefunden.")

# 📌 Hauptmenü
def hauptmenue():
    begruessung()
    while True:
        print("🧭 Was möchtest du tun?")
        print("1️⃣  Kontakt hinzufügen")
        print("2️⃣  Kontakte anzeigen")
        print("3️⃣  Kontakte speichern")
        print("4️⃣  Kontakte laden")
        print("5️⃣  Kontakt aktualisieren")
        print("6️⃣  Beenden")

        wahl = input("➡️ Deine Auswahl: ")

        if wahl == "1":
            kontakt_hinzufuegen()
        elif wahl == "2":
            kontakte_anzeigen()
        elif wahl == "3":
            kontakte_speichern()
        elif wahl == "4":
            kontakte_laden()
        elif wahl == "5":
            kontakt_aktualisieren()
        elif wahl == "6":
            print("👋 Auf Wiedersehen!")
            break
        else:
            print("⚠️ Ungültige Auswahl, bitte erneut versuchen.")

# ▶️ Programmstart
hauptmenue()
