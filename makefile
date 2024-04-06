.EXPORT_ALL_VARIABLES:

# Install dependencies
install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

# Run the application in development mode
start_backend:
	cd backend && uvicorn websrv:app --reload --host 0.0.0.0 --port 3000

start_frontend:
	cd frontend && npm run serve

start:
	make start_backend & make start_frontend

# Code quality
format:
	# -----  Formatting Python code with Black
	cd backend && black .

	# -----  Formatting JavaScript code with Prettier
	cd frontend && npm run prettier

check:
	# -----  Validating Black code style
	cd backend && black --check --diff .

	# -----  Validating Flake8 code style
	cd backend && flake8 .

	# -----  Validating Prettier code style
	cd frontend && npm run prettier:check

	# -----  Validating CSpell errors
	cspell --no-progress .

	# ----- The code is formatted correctly