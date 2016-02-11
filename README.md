https://ottawa-city-jobs.herokuapp.com/
##Projects
this is the project django project for https://ottawa-city-jobs.herokuapp.com/

##Structure of the app

```
.
├── applications
		├── admin.py
		├── apps.py
		├── __init__.py
		├── locale/
		├── migrations/
		├── models.py
		├── __pycache__
		├── templates/
		├── test_emplois.py
		├── tests.py
		├── urls.py
		├── utils.py
		└── views.py
├── cache
├── db.sqlite3
├── fixtures
├── LICENSE
├── locale
├── manage.py
├── ottawacityjobs/
		├── conftest.py
		├── __init__.py
		├── __pycache__
		├── settings.py
		├── test_settings.py
		├── urls.py
		└── wsgi.py
├── Procfile
├── pytest.ini
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
└── static




9 directories, 20 files
```

###Installation

```
mkdir ottawacityjobs 
cd ottawacityjobs
virtualenv env_python_34
source env_python_34/bin/activate
git clone git@github.com:guinslym/django-ottawa-city-jobs.git
cd django-ottawa-city-jobs
python manage.py runserver 8001
```