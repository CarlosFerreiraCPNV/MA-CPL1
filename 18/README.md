# Exercice 18 — Recherche des 3 emails les plus proches

## Fichier à rendre
- `n8n-Similitude.json`

## Ce que fait le workflow
- reçoit un email Outlook
- génère son embedding via l’API Ollama
- lit un corpus local d’emails déjà vectorisés
- calcule la similarité cosinus
- retourne les 3 emails les plus proches

## JSON de sortie à mettre dans le README
```json
[
  {
    "subject": "Demande de rendez-vous",
    "body_text": "Bonjour, seriez-vous disponible mardi prochain ?",
    "sender": "client1@example.com",
    "similarity": 0.92
  },
  {
    "subject": "Planification d'une réunion",
    "body_text": "J’aimerais organiser un point la semaine prochaine.",
    "sender": "client2@example.com",
    "similarity": 0.89
  },
  {
    "subject": "Disponibilités pour un entretien",
    "body_text": "Pouvez-vous me proposer un créneau ?",
    "sender": "client3@example.com",
    "similarity": 0.87
  }
]
```

## Remarque pratique
Le code final peut aussi ajouter :
- `incoming_subject`
- `incoming_body_text`
- `incoming_sender`

comme ça, l’exercice 19 peut réutiliser directement les données du mail entrant.
