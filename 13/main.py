import csv
import requests

# Adresse du serveur Ollama sur le réseau
API_URL = "http://10.229.43.154:11434/api/generate"

# Nom du modèle utilisé
MODEL_NAME = "mistral"


def analyse_message(texte):
    prompt = f"""
Analyse le message et réponds uniquement par Oui ou Non.

Réponds "Oui" si le message nécessite une réponse.
Réponds "Non" sinon.

Message : {texte}
"""

    response = requests.post(
        API_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    data = response.json()

    return data["response"].strip()


def main():
    score = 0
    total = 0

    with open("emails.csv", "r", encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)

        for row in reader:
            email_text = row["email_text"]
            label_attendu = row["label_attendu"]

            resultat = analyse_message(email_text)

            print("Message :", email_text)
            print("Réponse IA :", resultat)
            print("Réponse attendue :", label_attendu)

            if resultat == label_attendu:
                print("Résultat : correct")
                score += 1
            else:
                print("Résultat : incorrect")

            print("-" * 40)
            total += 1

    print(f"Score final : {score}/{total}")


if __name__ == "__main__":
    main()