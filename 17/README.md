# Exercice 17 — Création d’Embeddings de mails

## Fichier à rendre
- `TP3-Embedding.json`

## Étapes du workflow
1. **Outlook** : récupère plusieurs emails avec **Get Many Messages**.
2. **Code** : prépare `text_for_embedding` avec le préfixe `search_document:`.
3. **HTTP Request** : appelle `http://gpu.cpnv.me:11434/api/embeddings` avec `nomic-embed-text-v2-moe`.
4. **Merge** : combine les données du mail et le résultat de l’API par position.
5. **Code** : transforme le résultat final en une ligne JSON sérialisée.
6. **Convert to File** : génère `embeddingsVotreNom.json`.
7. **Read/Write Files from Disk** : écrit `/data/embeddingsVotreNom.jsonl`.

## JSON de sortie à mettre dans le README
```json
{
  "line": "{"message_id":"abc123","conversation_id":"conv456","mailbox":"etudiant@cpnv.me","sender":"prof@cpnv.me","recipients":"etudiant@cpnv.me","subject":"Rendez-vous","body_text":"Bonjour, peut-on fixer un rendez-vous ?","has_attachments":false,"text_for_embedding":"search_document: Objet: Rendez-vous\nExpéditeur: prof@cpnv.me\nDestinataire(s): etudiant@cpnv.me\nMessage:\nBonjour, peut-on fixer un rendez-vous ?","embedding_model":"nomic-embed-text-v2-moe","embedding":[0.012,-0.084,0.331],"created_at":"2026-03-27T09:00:00.000Z"}"
}
```

## Remarques
- Le champ `embedding` doit prendre `j.embeddings[0]`.
- Le vecteur ci-dessus est un exemple raccourci pour le README.
