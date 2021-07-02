#!/bin/bash

printf "Setup a Environment..."
virtualenv -p python3.6 env
source env/bin/activate
pip install -r requirements.txt

if test ! -d "./output"; then
    mkdir output
fi
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
tar -zxvf geckodriver-v0.29.1-linux64.tar.gz
rm geckodriver-v0.29.1-linux64.tar.gz
printf "Completed.\n"

printf "Migrate..."
python manage.py makemigrations
python manage.py migrate
printf "Completed.\n"

printf "Load data..."
python manage.py loaddata --app extra_table extra_table.json
printf "Completed.\n"

printf "Add crobtab..."
python manage.py crontab add
printf "Completed.\n"
