default: help

bootstrap: ## install the project dependencies
	yarn install
.PHONY: bootstrap

dev: ## start the dev environment
	yarn run android
.PHONY: dev

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help
