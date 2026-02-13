import re
import csv
import os

FICHIER = "mots.csv"

def check_word(fichier, mot):
    """Vérifie si le mot est déjà présent (insensible à la casse)."""
    if not os.path.exists(fichier):
        return False

    with open(fichier, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["mot"].strip().lower() == mot.strip().lower():
                return True
    return False


def get_next_id(fichier):
    """Récupère le prochain ID."""
    if not os.path.exists(fichier) or os.stat(fichier).st_size == 0:
        return 1

    with open(fichier, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ids = [int(row["id"]) for row in reader]

        if not ids:
            return 1

        return max(ids) + 1


def add_word(mot):
    """Ajoute un mot uniquement s'il n'existe pas déjà."""
    if check_word(FICHIER, mot):
        print(f"❌ Le mot '{mot}' existe déjà dans le CSV.")
        return

    next_id = get_next_id(FICHIER)
    file_exists = os.path.exists(FICHIER)

    with open(FICHIER, mode="a", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "mot"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists or os.stat(FICHIER).st_size == 0:
            writer.writeheader()

        writer.writerow({
            "id": next_id,
            "mot": mot.strip()
        })

    print(f"✅ Mot '{mot}' ajouté avec ID = {next_id}")


def show_csv():
    if not os.path.exists(FICHIER) or os.stat(FICHIER).st_size == 0:
        print("📭 Le fichier CSV est vide ou n'existe pas.")
        return

    with open(FICHIER, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        print("\n📄 Contenu du fichier :\n")
        for row in reader:
            print(f"ID: {row['id']}  |  Mot: {row['mot']}")


txt = input("Texte à tokenizer :")
text_split = re.findall(r"[A-Za-zÀ-ÿ0-9]+|[^A-Za-zÀ-ÿ0-9\s]", txt)

for x in range(len(text_split)):
    add_word(text_split[x])

show_csv()
