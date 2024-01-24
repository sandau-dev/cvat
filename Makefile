export CVAT_VERSION := v2.10.0
export CVAT_DATA_MNT_PATH := /media/ph1ash/Storage/cvat_cvat_data/
# export CVAT_DATA_MNT_PATH := /mnt/azure_nfs/sandau_cvat_docker/cvat_cvat_data/
export ACME_EMAIL := matt@sandau.dev
export CVAT_HOST := 192.168.1.192
# export CVAT_HOST := asbuilt.cvat.sandau.dev

build:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

run:
	docker compose -f docker-compose.yml -f docker-compose.https.yml up -d

run-serverless-dev:
	docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d --force-recreate

run-serverless:
	docker compose -f docker-compose.yml -f docker-compose.https.yml -f components/serverless/docker-compose.serverless.yml up -d

stop:
	docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml down

logs:
	docker compose logs -f
