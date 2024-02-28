# INJOZI BACKEND ASSESSMENT

Python Flask Restful JWT Authentication with MongoDB

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes.

### Prerequisites

Before you can run this project you need a install python first on your operating system.
You can download python [here](https://www.python.org/downloads/) and choose according to your operating system.
n addition you also need a MongoDB NoSQL database and you can download
[here](https://www.mongodb.com/download-center/community).

### Installing

First, clone this project from github using git command or git gui application like [fork](https://git-fork.com/).

```
$ git clone https://github.com/Bigveezus/Injozi-Bit.git
```

Making environment for project to isolation python installing libraries for this project only.

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

**Make sure you are inside the virtual env in your terminal**

- Then install the requirements
  Installing all libraries needed by this project using [pip](https://pypi.org/project/pip/).

```
$ pip install -r requirements.txt
```

Make a configuration file with name _.env_ with this configuration (_change as desired_).

```
MONGODB_SETTINGS = { 'host': 'mongodb://localhost/injozi-bit' }
JWT_SECRET_KEY = 'injozi'
```

Setting the environment for this project.

```
$ export FLASK_APP=app.py
$ export ENV_FILE_LOCATION=./.env
```

Running the project.

```
flask run
```

To test crud api endpoint that has been created you can use **curl** utility. Before test, you must login
first to get jwt token and using it in every request header you sent.

```
$ curl -X POST localhost:5000/api/v1/login -d '{"username":"super@injozi.net", "password":"injozi"}' -H "Content-Type: application/json"
```

- THE REST OF THE DOCUMENTATION CAN BE FOUND HERE AT https://documenter.getpostman.com/view/21609093/2sA2rFTLrT

## To run docker

To run docker, all you need is to have docker running on your system then in your root folder in the terminal run `docker compose up` and it runs and exposes on port `http://localhost:5000/`
