export CVAT_VERSION := v2.10.0
export CVAT_DATA_MNT_PATH := /mnt/azure_nfs/sandau_cvat_docker/cvat_cvat_data/
export ACME_EMAIL := matt@sandau.dev
export CVAT_HOST := asbuilt.cvat.sandau.dev

build:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

run:
	docker compose -f docker-compose.yml -f docker-compose.https.yml up -d

stop:
	docker compose down

logs:
	docker compose logs -f
