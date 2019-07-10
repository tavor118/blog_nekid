# blog_nekid
Blog project. Python 3.6, Django 2.1

## Install
For the next steps of service installation, you will need setup of Ubuntu OS

### Manual installation
* Create new directory
* Create a new virtual environment with `Python 3.6` 
(using `pyenv`, `venv`, `virtualenv`  or another tool).
* Clone this repository to your local machine
```commandline
git clone https://github.com/tavor118/blog_nekid.git
cd blog_nekid/blog_nekid
```

### Django

* Install requirement project's packages (for local development)
```commandline
pip install --upgrade pip
pip install -r requirements.txt
```

* Go to the folder with `manage.py` file and run migrate files
```
python manage.py migrate
```

* For populating database run bot 
```
python manage.py bot
```

* Go to the folder with `manage.py` file, run django server 
( By default, the server runs on port 8000 on the IP address 127.0.0.1.)

```
python manage.py runserver
```
* Link: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


* For pylint check
```commandline
PYTHONPATH=$PYTHONPATH:`pwd`
export PYTHONPATH
pylint --rcfile=.pylintrc *
```

### Installation via Docker

* Clone this repository to your local machine
```commandline
git clone https://github.com/tavor118/blog_nekid.git
cd blog_nekid/
```

* Run docker-compose
```commandline
docker-compose up -d --build
```
* Link: [http://localhost:8990/](http://localhost:8990/)