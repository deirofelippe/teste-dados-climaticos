init-tmp-container:
	@docker container run -it --rm --name app-dados -v $$(pwd)/:/home/jovyan/work -w /home/jovyan/work quay.io/jupyter/datascience-notebook:2024-08-30 bash

gen-reqs:
	@conda list -e > ./requirements.txt

conda-install:
	@conda install --file ./requirements.txt

py-server:
	@python src/server.py

py-client:
	@python src/client.py

## DOCKER

ps:
	@docker compose ps -a

logs:
	@docker compose logs -f app-dados

reload: down up

up:
	@docker compose up -d --build

down:
	@docker compose down

token:
	@docker compose logs app-dados | grep 'http://127.0.0.1:8888/lab?token=' | head -n 1 | awk '{ print $$(NF)}'

exec:
	@docker compose exec -it app-dados bash

exec-root:
	@docker compose exec -it --user root app-dados bash