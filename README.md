# EquipIT

EquipIT is a Django web application for consulting and lending IT equipment. It provides a REST API for equipment listing and lending operations, plus an interface ready to consume the API.

## Prerequisites

- Python 3.14+
- uv
- PostgreSQL 18 for the target environment

SQLite is used automatically for local development when `DATABASE_URL` is not defined.

## Installation

```bash
uv sync
cp .env.example .env
uv run python manage.py migrate
```

## Run

```bash
uv run python manage.py runserver
```

API documentation is available at `/docs/` and the OpenAPI schema at `/schema/`.

## API

- `GET /api/equipment/`
- `PUT /api/equipment/<id>/borrow/`
- `PUT /api/equipment/<id>/return/`

## Project structure

- `config/`: Django project configuration and root URLs
- `equipment/models.py`: persistence model
- `equipment/services.py`: business operations
- `equipment/serializers.py`: API input and output validation
- `equipment/views.py`: HTTP API layer
- `equipment/tests/`: automated tests
- `templates/`: web interface templates

## Tests and quality

```bash
uv run pytest
uv run ruff check .
```

## License

This project is distributed under the MIT License.
