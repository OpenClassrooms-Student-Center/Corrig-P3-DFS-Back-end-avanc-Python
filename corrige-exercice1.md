# Exercice 1 : Logique métier Django

## Objectif pédagogique

Implémenter les opérations d'emprunt et de retour dans un service isolé de la couche HTTP.

## Étape 1 : Recherche

`EquipmentService.find_equipment` centralise la recherche et le cas de ressource inexistante.

## Étape 2 : Emprunt

L'opération contrôle la disponibilité, normalise les noms, renseigne la date d'emprunt et sauvegarde les champs concernés.

## Étape 3 : Retour

L'opération contrôle l'état courant, réinitialise les informations de l'emprunteur et renseigne la date de retour.

## Étape 4 : Tests

Les tests du service couvrent les transitions valides et les erreurs métier.