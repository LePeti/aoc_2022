.PHONY: help build shell test format clean

.DEFAULT: help

help: ## Print this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

test: ## Run flake8 syntax and codestyle check, then run tests with pytest
	# flake8 src
	pytest tests
	# make clean

format: ## Format with black, then run flake8 syntax and codestyle check
	black src tests
	flake8 src tests

clean: ## Delete /.pytest_cache and tests/__pycache__
	rm -rf .pytest_cache
	rm -rf **/__pycache__

add-package: ## Install latest python package and add to requirements. Usage: make add-package package=<package_name>
	pip install $(package)
	pip freeze | grep -i $(package) >> requirements.txt

create-daily-files: ## Create day_x.py under the `src` and `input` folders. Usage: `make create-daily-files day=5`
	touch src/day_$(day).py
	touch input/day_$(day).py
