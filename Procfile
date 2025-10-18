release: python manage.py migrate && python fixtures/load_fixtures.py
web: gunicorn quiz.wsgi --log-file -
