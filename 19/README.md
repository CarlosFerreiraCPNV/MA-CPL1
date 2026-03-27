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
1. **Build RAG Prompt** : construit un prompt clair avec l’email reçu, les 3 emails similaires et une consigne stricte.
2. **HTTP Request - Generate Reply** : appelle `http://gpu.cpnv.me:11434/api/generate`.
3. **Format Generated Reply** : extrait `response` et le renomme en `generated_reply`.

## JSON de sortie à mettre dans le README
```json
{
  "generated_reply": "Bonjour,

Merci pour votre message. Je vous propose de convenir d’un rendez-vous la semaine prochaine selon vos disponibilités. Merci de m’indiquer les créneaux qui vous conviennent.

Cordialement"
}
```

## Conseil
Pour éviter les réponses inventées, ajoute dans le prompt :
- `N'invente pas d'informations absentes du contexte.`
- `Réponds en français.`
- `Sois professionnel et concis.`
