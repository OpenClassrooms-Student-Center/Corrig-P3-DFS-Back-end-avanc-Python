# Erreurs fréquentes

- Placer la règle de disponibilité directement dans la vue.
- Oublier de sauvegarder la date d'emprunt.
- Ne pas vider les informations de l'emprunteur au retour.
- Retourner `200` pour une ressource inexistante.
- Utiliser `request.data` sans serializer.
- Dupliquer les règles métier dans plusieurs endpoints.
- Oublier les migrations après modification du modèle.
- Tester uniquement le cas nominal.