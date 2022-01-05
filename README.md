Prerequisite
1. Already installed MySQL with database named cdatabase in it.
2. Python 3 installed

1. Create python virtual environment
    $ > python3 -m venv .env

2. Activate virtual environment
    $ > .\.env\Scripts\activate

3. Install all python library to the virtual environment
     (.venv)  pip install -r .\requirements.txt

4. Initiate database 
     (.venv) flask db init
     (.venv) flask db migrate -m 'article model'
     (.venv) flask db upgrade

5. Run flask as python microservice backend
    (.venv) flask run