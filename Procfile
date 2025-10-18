release: python manage.py migrate && python fixtures/load_fixtures.py && python setup_data/restore_essential_data.py
web: gunicorn quiz.wsgi --log-file -
