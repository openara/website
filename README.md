# website

** Installation **

 - install python 2.7

In the directory where you have cloned the repo,

Create a virtualenv to collect python packages
    
    virtualenv --no-site-packages .

Enter the virtualenv context

    source bin/activate

Install the required packages

    pip install -r requirements.txt


Create the database:

    python manage.py migrate


Finally run the server localy:

    python manage.py runserver

