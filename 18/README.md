
# Exercice 18 — Recherche des 3 emails les plus proches

## Fichier à rendre
- `n8n-Similitude.json`

## Ce que fait le workflow
- reçoit un email Outlook
- génère son embedding via l’API Ollama
- lit un corpus local d’emails déjà vectorisés
- calcule la similarité cosinus
- retourne les 3 emails les plus proches

## Résultat attendu
Le dernier node retourne 3 items avec :
- `subject`
- `body_text`
- `sender`
- `similarity`

## Remarque pratique
Le code final ajoute aussi :
- `incoming_subject`
- `incoming_body_text`
- `incoming_sender`

comme ça, l’exercice 19 (RAG) peut réutiliser directement les données du mail entrant.
