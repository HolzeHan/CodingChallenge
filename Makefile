build:
	docker compose build

up:
	docker compose up -d

run-example:
	docker compose run --entrypoint=python merge entrypoint.py [25,30] [2,19] [14,23] [4,8]

test: 
	docker compose run --entrypoint=pytest merge
