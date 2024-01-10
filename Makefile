export CVAT_VERSION := v2.10.0

build:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

run:
	docker compose -f docker-compose.yml -f docker-compose.https.yml up -d

stop:
	docker compose down

logs:
	docker compose logs -f