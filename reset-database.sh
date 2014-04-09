#!/bin/bash

. venv/bin/activate
cat idb/database.py > deleteme.txt
echo -e "\nreset_database()" >> deleteme.txt
python manage.py shell < deleteme.txt
rm -f deleteme.txt
