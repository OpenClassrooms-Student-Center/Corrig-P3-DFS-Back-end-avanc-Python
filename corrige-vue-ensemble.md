# Vue d'ensemble du corrigé EquipIT

La solution sépare les règles métier, la persistance, la validation HTTP et le transport REST.

## Résultats attendus

- L'emprunt vérifie la disponibilité, enregistre l'identité et la date.
- Le retour vérifie que l'équipement est emprunté, restaure sa disponibilité et conserve la date de retour.
- Les erreurs métier sont traduites par la couche API en réponses HTTP lisibles.
- Les tests couvrent les cas nominaux, les ressources inconnues et les transitions invalides.