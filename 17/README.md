
# Exercice 17 — Création d’Embeddings de mails

## Fichier à rendre
- `TP3-Embedding.json`

## Étapes du workflow
1. **Récupère les messages Outlook** : lit plusieurs emails depuis Outlook.
2. **Crée un texte condensé du mail** : prépare `text_for_embedding` avec le préfixe `search_document:`.
3. **Calcul de l'embedding** : appelle `http://gpu.cpnv.me:11434/api/embeddings` avec le modèle `nomic-embed-text-v2-moe`.
4. **Merge** : combine les données du mail et le résultat de l’API par position.
5. **Transforme les données** : crée un objet final avec `message_id`, `subject`, `body_text`, `embedding`, `created_at`, etc.
6. **Convertit en un fichier** : génère `embeddingsVotreNom.json`.
7. **Écrit sur le disque** : sauvegarde dans `/data/embeddingsVotreNom.jsonl`.

## Point important
Le champ `embedding` doit prendre `j.embeddings[0]` pour enregistrer le vecteur du mail.
