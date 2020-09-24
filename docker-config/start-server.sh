#!/bin/bash

CONTAINER_ALREADY_STARTED="/CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    echo "-- First container startup --"
    # YOUR_JUST_ONCE_LOGIC_HERE
    conda env create -f django.yml
    source activate django
    python3 manage.py migrate
else
    echo "-- Not first container startup --"
    source activate django
fi
python3 manage.py runserver 0.0.0.0:8000
