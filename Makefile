-include .env
export

DEV_HOST ?= 0.0.0.0
DEV_PORT ?= 8000

serve:
	uv run mkdocs serve --dev-addr $(DEV_HOST):$(DEV_PORT)
