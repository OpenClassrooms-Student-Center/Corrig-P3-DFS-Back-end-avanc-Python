# FAQ étudiants

## Pourquoi un service séparé ?

Pour isoler les règles métier du transport HTTP et pouvoir les tester indépendamment.

## Pourquoi un serializer ?

Pour valider explicitement la forme et les contraintes des données reçues par l'API.

## Pourquoi une transaction ?

Pour garantir qu'une opération métier complète est validée ou annulée dans son ensemble.

## Quel statut utiliser pour un équipement inconnu ?

L'API renvoie `404 Not Found` sans exposer l'exception interne.