
# Exercice 15 — Classification automatique d’emails avec n8n et IA

## Fichier à rendre
- `TP1_Email_Classifier.json`

## Workflow
1. **Microsoft Outlook Trigger** : déclenchement à la réception d’un nouvel email.
2. **Prépare données** : construit `emailText` à partir de `subject`, `bodyPreview`, `from` et `id`.
3. **Envois à API Ollama** : appelle `http://gpu.cpnv.me:11434/api/generate` avec le modèle `Matheswaran/email-classifier:latest`.
4. **Mise en forme données** : lit `response` et retourne :
   - `requestType`
   - `requestSubType`
   - `confidenceScore`
   - `reasoning`
   - `outlookCategory`

## Exemple de résultat attendu
```json
{
  "requestType": "Appointment Request",
  "requestSubType": "Meeting Request",
  "confidenceScore": 95,
  "reasoning": "The email subject and the body text of the email suggest that the sender is requesting a meeting.",
  "outlookCategory": "Appointment Request"
}
```

## Remarques
- Le node HTTP Request doit envoyer un JSON avec `model`, `prompt` et `stream: false`.
- Le prompt doit demander **du JSON uniquement**.
- Dans n8n, adapte les credentials Outlook OAuth2 avant d’exécuter.
