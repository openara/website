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


Create a superuser:

    python manage.py createsuperuser


Run the server localy:

    python manage.py runserver


Log in the admin:

    http://localhost:8000/admin/
    


Add a first language ( fixtures don't load actually ... may be fixed soon )


Publish the root item to provide access to public users ( otherwise, '/' is 404 when you logg off )
    
    
    
    
    
