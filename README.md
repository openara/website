# Site internet des Makerspace et Fablab de la région Auverge-Rhône-Alpes

## Installation

1. Install python 2.7

2. In the directory where you have cloned the repo,
create a virtualenv to collect python packages
    
    virtualenv --no-site-packages .

3. Enter the virtualenv context

    source bin/activate

4. Install the required packages

    pip install -r requirements.txt


5. Create the database:

    python manage.py migrate


6. Finally run the server localy:

    python manage.py runserver