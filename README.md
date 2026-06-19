# Account Health Tracker

A REST API for managing reseller accounts across multiple platforms. It tracks account metadata and purchase history, with the goal of computing a dynamic "health" status per account — indicating whether an account is ready to use, in cooldown, or exhausted.

Built as a backend portfolio project to demonstrate FastAPI, SQLAlchemy, and clean API design.

## Tech Stack

- **FastAPI** — web framework and automatic OpenAPI docs
- **SQLAlchemy** — ORM for database interaction
- **SQLite** — local database (file-based, no setup required)
- **Pydantic** — request/response validation via schemas

## Setup

**1. Clone the repo and create a virtual environment**

```bash
git clone https://github.com/simonpozgay/account-health-tracker.git
cd account-health-tracker
python -m venv venv
```

**2. Activate the virtual environment**

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install fastapi sqlalchemy uvicorn pydantic
```

**4. Run the server**

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs are at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/accounts` | List all accounts |
| `GET` | `/accounts/{id}` | Get a single account by ID |
| `POST` | `/accounts` | Create a new account |
| `DELETE` | `/accounts/{id}` | Delete an account by ID |

### Example: Create an account

```http
POST /accounts
Content-Type: application/json

{
  "email": "user@example.com",
  "platform": "PlatformName"
}
```

### Example response

```json
{
  "id": 1,
  "email": "user@example.com",
  "platform": "PlatformName",
  "last_purchase_date": null
}
```

> Note: `email` + `platform` is enforced as a unique pair — you can't register the same account twice on the same platform.

## Future Roadmap

- **Purchase history endpoints** — `POST /accounts/{id}/purchases`, `GET /accounts/{id}/purchases` to log and retrieve purchases per account
- **Computed account status** — derive a `status` field at read-time based on `last_purchase_date` (e.g. `HEALTHY`, `COOLDOWN`, `EXHAUSTED`) rather than storing it
- **PostgreSQL support** — swap out SQLite for Postgres for production-readiness


## AI Usage Declaration

This project was built with Claude as a learning tool:
- Used to explain FastAPI/SQLAlchemy concepts I was unfamiliar with
- Used to generate this README based on the project's actual codebase

All code was written and understood by me — AI was used for learning, not to generate unreviewed code.
