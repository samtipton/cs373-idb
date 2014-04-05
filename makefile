
all:
	python manage.py collectstatic
	python manage.py sqlall idb > schema.sql
	git push heroku master

clean:
	rm -f *.pyc
	rm -fr __pycache__
