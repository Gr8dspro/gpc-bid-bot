# gpc-bid-bot (minimal bootstrap)
Shadow → semi-auto GPC micro-quote bot. Rules live in `packages/rules/schema.yaml`.
## Dev
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
