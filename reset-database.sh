#!/bin/bash

echo -e 'from idb.database import reset_database\nreset_database()' | python manage.py shell
python manage.py installwatson
python manage.py buildwatson
