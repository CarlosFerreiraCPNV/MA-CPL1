# Réponses – TP_12 YOLO & analyse d'image

## 1. Quels sont les types d'objets détectés dans l'image ?
L'image montre principalement **une voiture**. Avec YOLO, on s'attend donc à obtenir au moins une détection de type **car**.

## 2. Le niveau de confiance est-il élevé ou faible ?
On s'attend à un **niveau de confiance élevé**, car :
- l'objet est bien visible,
- il occupe une grande partie de l'image,
- l'arrière-plan est simple,
- la voiture n'est pas cachée.

## 3. YOLO a-t-il commis des erreurs visibles ?
Sur ce type d'image, YOLO ne devrait pas faire beaucoup d'erreurs. Une erreur possible serait :
- une boîte un peu trop grande ou trop petite,
- une seule détection alors que certains détails de la voiture pourraient prêter à confusion,
- ou au contraire une détection parasite sur une zone brillante.

## 4. Quel serait un cas où YOLO ne fonctionnerait pas bien ?
YOLO fonctionne moins bien si :
- l'objet est flou,
- l'objet est très petit,
- l'image est sombre,
- plusieurs objets se cachent partiellement,
- l'objet est vu sous un angle inhabituel,
- ou l'objet n'appartient pas aux classes apprises par le modèle.

## Remarque importante
Dans cet environnement, l'extraction de l'image jointe a bien fonctionné, mais l'exécution complète de YOLO n'a pas pu être finalisée car le poids `yolov8n.pt` ne peut pas être téléchargé hors ligne. Sur un PC connecté à Internet, les scripts fournis permettent de générer :
- l'image annotée,
- le fichier `detections.json`.
