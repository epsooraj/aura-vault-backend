COMPOSE_DEPS_FILE=docker/docker-compose.deps.yml
DC_DEPS=docker compose -f $(COMPOSE_DEPS_FILE)
PYTHON=./venv/bin/python

.PHONY: deps-up deps-down deps-logs deps-ps runserver

deps-up:
	$(DC_DEPS) up -d

deps-down:
	$(DC_DEPS) down

deps-logs:
	$(DC_DEPS) logs -f

deps-ps:
	$(DC_DEPS) ps

runserver:
	$(PYTHON) manage.py runserver

