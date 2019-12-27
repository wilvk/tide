.PHONY: tests clean git-install build upload local-dev docker-dev pylint

define DOCKER_COMPOSE
docker-compose -f ./tests/docker/docker-compose.yml build
docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports 
endef

define DOCKER_COMPOSE_SHIPPABLE
docker-compose -f /app/tests/docker/docker-compose.yml build
docker-compose -f /app/tests/docker/docker-compose.yml run --rm --service-ports 
endef

tests:
	$(DOCKER_COMPOSE) test-python-tide /work/tests/scripts/run-python-tests

tests-shippable:
	$(DOCKER_COMPOSE) test-python-tide-shippable sh -c "cd /app && ls -alh"

#/app/tests/scripts/run-python-tests

clean:
	rm -rf dist
	rm -rf tide.egg-info
	rm -rf build

git-install:
	git submodule init
	git submodule update

build:
	$(DOCKER_COMPOSE) test-python-tide /work/tests/scripts/run-build-package

upload:
	$(DOCKER_COMPOSE) test-python-tide /work/tests/scripts/run-upload-package

local-dev:
	pip install -e .

docker-dev:
	$(DOCKER_COMPOSE) test-python-tide sh

pylint:
	docker run --rm -v $(PWD)/tide:/code eeacms/pylint --rcfile=/code/.pylintrc /code
