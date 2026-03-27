
# Exercice 19 — Génération de réponse email avec RAG

## Fichier à rendre
- `n8n-RAG-Email.json`

## Pré-requis
Ce workflow part du résultat de l’exercice de similitude, qui fournit :
- `incoming_subject`
- `incoming_body_text`
- `incoming_sender`
- 3 emails similaires avec `subject`, `body_text`, `similarity`

## Nodes ajoutés
1. **Build RAG Prompt** : construit un prompt clair avec :
   - l’email reçu
   - les 3 emails similaires
   - une consigne stricte : répondre en français, professionnellement, sans inventer
2. **HTTP Request - Generate Reply** : appelle `http://gpu.cpnv.me:11434/api/generate`
3. **Format Generated Reply** : extrait `response` et le renomme en `generated_reply`

## Exemple de sortie finale
```json
{
  "generated_reply": "Bonjour,

Merci pour votre message..."
}
```

## Conseil
Si les réponses sont trop longues ou trop inventées, raccourcis le prompt et ajoute une règle du style :
`Réponds en 5 phrases maximum.`
