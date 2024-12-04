export CVAT_VERSION := v2.23.0
export CVAT_DATA_MNT_PATH := /var/nfs/nfs_storage/cvat_data/
#export CVAT_DATA_MNT_PATH := /mnt/azure_nfs/sandau_cvat_docker/cvat_cvat_data/
export ACME_EMAIL := matt@sandau.dev
export CVAT_HOST := dextop.local
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

deploy-sam:
	cd serverless && ./deploy_gpu.sh pytorch/facebookresearch/segment_anything_2/nuclio/

deploy-yolo:
	cd serverless && ./deploy_gpu.sh pytorch/ultralytics/yolov8/nuclio/

logs:
	docker compose logs -f
