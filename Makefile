# Makefile for Quiz Project

.PHONY: help install test test-cov test-fast lint format clean migrate run

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install all dependencies including dev
	uv pip install -e ".[dev]"

install-prod:  ## Install only production dependencies
	uv pip install -e "."

test:  ## Run all tests with coverage
	uv run pytest

test-cov:  ## Run tests and generate HTML coverage report
	uv run pytest --cov --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

test-fast:  ## Run tests in parallel (faster)
	uv run pytest -n auto

test-unit:  ## Run only unit tests
	uv run pytest quizzes/tests/unit/

test-integration:  ## Run only integration tests
	uv run pytest quizzes/tests/integration/

test-models:  ## Run only model tests
	uv run pytest quizzes/tests/unit/test_models_*.py

test-views:  ## Run only view tests
	uv run pytest quizzes/tests/unit/test_views.py

test-services:  ## Run only service tests
	uv run pytest quizzes/tests/unit/test_services.py

test-watch:  ## Run tests in watch mode
	pytest-watch

lint:  ## Run all linters
	@echo "Running flake8..."
	flake8 quizzes/
	@echo "Running mypy..."
	mypy quizzes/
	@echo "Running pylint..."
	pylint quizzes/
	@echo "Running bandit..."
	bandit -r quizzes/ -ll

format:  ## Format code with black and isort
	black quizzes/
	isort quizzes/

format-check:  ## Check if code is formatted correctly
	black --check quizzes/
	isort --check-only quizzes/

clean:  ## Remove all build, test, coverage and Python artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*~" -delete
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info

migrate:  ## Run database migrations
	uv run python manage.py makemigrations
	uv run python manage.py migrate

run:  ## Run development server
	uv run python manage.py runserver

shell:  ## Open Django shell
	python manage.py shell

createsuperuser:  ## Create superuser
	python manage.py createsuperuser

collectstatic:  ## Collect static files
	python manage.py collectstatic --noinput

check:  ## Run Django system checks
	python manage.py check

security-check:  ## Run security checks
	bandit -r quizzes/ -ll
	safety check

ci:  ## Run CI pipeline (format check + lint + test)
	@make format-check
	@make lint
	@make test-cov

coverage-report:  ## Open coverage report in browser
	open htmlcov/index.html

db-reset:  ## Reset database (WARNING: deletes all data)
	python manage.py flush --no-input
	python manage.py migrate

db-seed:  ## Seed database with test data
	python manage.py loaddata fixtures/*.json

upgrade-deps:  ## Upgrade all dependencies
	uv pip install --upgrade -e ".[dev]"

.DEFAULT_GOAL := help
