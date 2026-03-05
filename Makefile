-include .env
export

DEV_HOST ?= 0.0.0.0
DEV_PORT ?= 8000

serve:
	@lsof -ti:$(DEV_PORT) | xargs kill -9 2>/dev/null || true
	PYTHONPATH=$(CURDIR) uv run python scripts/dev_serve.py --dev-addr $(DEV_HOST):$(DEV_PORT)
