# Movies App

This is a Simple App for Building a CRUD about movies

## Description

The project idea is to learn and improve technical skill in python building a simple app with FastAPI framework.

## Getting Started


### Dependencies

Please make sure the following requirements are met before getting started

 - [git client](https://git-scm.com/downloads)
 - [Python](https://www.python.org/downloads/) == 3.9
 - python3-venv (Usually comes with python 3.3+ versions)

### Installing

Clone the app in a regular path and enter to the created folder

``` bash
$ git clone git@github.com:sarias12/movies-app.git
$ cd movies-app/
```

Create a new virtualenv to install the python required dependencies

```bash
python3 -m venv venv
```

Once the virtual environment is created, proceed to activate
```bash
$ source venv/bin/activate
(venv) $
```
Install python dependencies

```bash
(venv) $ pip install -r requirements.txt
```
### Executing program

Execute the following line to start the  local web server
```bash
make run-app --reload
```

Once you can the following message in your terminal:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2267] using StatReload
INFO:     Started server process [2269]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  StatReload detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [2269]
INFO:     Started server process [2320]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:42202 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:42202 - "GET /openapi.json HTTP/1.1" 200 OK
```
You can go to the following url [http//localhost:8080/](http//localhost:8080/) in your browser, there you will see all the documentation and information about the use of the API
## Authors

Sergio Steben Arias Quintero  
Email - steben.12q@gmail.com

## knowledges

* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/)
* [Python](https://www.python.org/)
* [Uvicorn](https://www.uvicorn.org/)

## Acknowledgments
* [Platzi](https://platzi.com/cursos/fastapi/)
