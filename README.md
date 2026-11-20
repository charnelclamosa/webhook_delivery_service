# Webhook Delivery Service

> **Status: Early development.** The Docker Compose stack, Make targets, and Alembic setup are in place. The API currently exposes a health check.

A Python service for accepting inventory events and delivering them as webhooks. The first demo will send a `tool.available` event to a receiver that returns `503` on the first attempt and `200` on the retry. The delivery status endpoint will show both attempts.

## Run locally

You’ll need Docker with Compose, Make, and curl. From the repository root, create an untracked `.env` file with these local development settings:

```dotenv
POSTGRES_DB=webhook
POSTGRES_USER=webhook
POSTGRES_PASSWORD=webhook_local_dev
DATABASE_URL=postgresql+psycopg://webhook:webhook_local_dev@postgres:5432/webhook
WEBHOOK_DESTINATION_URL=http://demo-receiver:8000/webhook
```

Build the shared Python image and start the API with its dependencies:

```bash
make build
docker compose --project-name webhook-delivery-service up -d api
curl -fsS http://localhost:8000/healthz
```

Compose starts PostgreSQL and runs `alembic upgrade head` before starting the API. The migration container exits after a successful run. Until the first schema revision lands, this step verifies the Alembic configuration and database connection.

Expected health response:

```json
{"status":"ok"}
```

## Make targets

| Command | Purpose |
| --- | --- |
| `make build` | Build the shared Python image. |
| `make run` | Start the full Compose stack. Use the API-only command above while the worker and demo receiver are being implemented. |
| `make logs` | Follow container logs. |
| `make bash` | Open a shell in the running API container. |
| `make stop` | Stop the stack and keep PostgreSQL data in its named volume. |

## Project layout

| Path | Purpose |
| --- | --- |
| `src/webhook_delivery/` | FastAPI entry point and modules for event submission, delivery, and retries |
| `migrations/` and `alembic.ini` | Database migration scripts and configuration |
| `compose.yaml` and `Dockerfile` | Local services and their shared Python image |
| `requirements.txt` | Python dependencies for the app, tests, and linting |
| `tests/` | Unit and PostgreSQL integration tests as they are added |

## Roadmap

- [ ] Create the PostgreSQL schema for events, deliveries, and delivery attempts.
- [ ] Add `POST /events` with idempotent submissions and `GET /deliveries/{delivery_id}` with attempt history.
- [ ] Implement the delivery worker, bounded retries, and recovery after a worker restart.
- [ ] Add the demo receiver, automated tests, and GitHub Actions.

See [PROJECT_SPECIFICATION.md](PROJECT_SPECIFICATION.md) for the development tasks and acceptance criteria.
