# EquipIT - Solution de référence

Cette version implémente les opérations métier d'emprunt et de retour, les endpoints REST et la validation des données avec Django REST Framework.

## Architecture

- `equipment/models.py` : entité persistée avec Django ORM.
- `equipment/services.py` : règles métier transactionnelles et exceptions métier.
- `equipment/serializers.py` : validation du payload d'emprunt.
- `equipment/views.py` : couche HTTP et traduction des erreurs en réponses REST.
- `equipment/tests/` : tests du service et tests d'intégration API.

## Validation

```bash
uv sync
uv run python manage.py migrate
uv run pytest
uv run ruff check .
```