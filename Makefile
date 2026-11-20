# ---- Configuration ----
PROJECT_NAME ?= webhook-delivery-service
SERVICE      ?= api
TEST         ?=

COMPOSE := docker compose --project-name $(PROJECT_NAME)

.DEFAULT_GOAL := all
.PHONY: all build run logs deploy test bash stop

all: build
	$(MAKE) run

build:
	$(COMPOSE) build api

run:
	$(COMPOSE) up -d

stop:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

test:
	$(COMPOSE) run --rm \
		--volume "$(CURDIR)/tests:/app/tests:ro" \
		api pytest -v -s --disable-pytest-warnings "tests/$(TEST)"

bash:
	$(COMPOSE) exec $(SERVICE) bash

deploy: build
	@echo "Deployment target not configured yet."