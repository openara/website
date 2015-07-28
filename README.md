## Site internet des Makerspace et Fablab de la région Auverge-Rhône-Alpes

### Installation

- Install python 2.7, virtualenv,libpython2.7-dev & postgresql-devel (libpq-dev in Debian/Ubuntu)

- In the directory where you have cloned the repo,
create a virtualenv to collect python packages
    
    virtualenv --no-site-packages .

- Enter the virtualenv context

    source bin/activate

- Install the required packages

    pip install -r requirements.txt


- Create the database:

    python manage.py migrate


- Finally run the server localy:

    python manage.py runserver
