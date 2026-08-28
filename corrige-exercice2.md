# Exercice 2 : API REST Django

## Objectif pédagogique

Structurer une API REST simple qui délègue les règles métier au service.

## Étape 1 : Organisation

Les serializers valident les données entrantes, les vues coordonnent la requête et le service effectue la mutation.

## Étape 2 : Endpoints

Les trois routes EquipIT sont exposées sous `/api/equipment/` avec les verbes HTTP prévus.

## Étape 3 : Gestion des erreurs

Les exceptions métier sont converties en réponses HTTP sans exposer de détails internes.

## Étape 4 : Vérification

Les tests API vérifient le parcours d'emprunt et le comportement d'une ressource inconnue.