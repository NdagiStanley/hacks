# hacks
Python Celery (PY checkins)

[![Build Status](https://semaphoreci.com/api/v1/stanmd/hacks/branches/develop/badge.svg)](https://semaphoreci.com/stanmd/hacks) [![Coverage Status](https://coveralls.io/repos/github/NdagiStanley/hacks/badge.svg?branch=develop)](https://coveralls.io/github/NdagiStanley/hacks?branch=develop) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/d8c3a5bb3ee84f50ba5032a7b3d9c458/badge.svg)](https://www.quantifiedcode.com/app/project/d8c3a5bb3ee84f50ba5032a7b3d9c458)
 [![Code Climate](https://codeclimate.com/github/NdagiStanley/hacks/badges/gpa.svg)](https://codeclimate.com/github/NdagiStanley/hacks) [![Issue Count](https://codeclimate.com/github/NdagiStanley/hacks/badges/issue_count.svg)](https://codeclimate.com/github/NdagiStanley/hacks) [![Code Health](https://landscape.io/github/NdagiStanley/hacks/develop/landscape.svg?style=flat)](https://landscape.io/github/NdagiStanley/hacks/develop)


##Prerequisites

Documentation of Celery Project [here](http://www.celeryproject.org/)

Message Transport Brokers like [RabbitMQ](https://www.rabbitmq.com/)

[Flask](http://flask.pocoo.org/docs/0.10/) microframework

##Getting started

In the terminal open four tabs:

**Tab 1**

Brew Install RabbitMQ as from this [reference](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#installation-configuration) by running:

- `brew update`

- `brew install rabbitmq`

- `echo PATH=$PATH:/usr/local/sbin`

Then run server

- `sudo rabbitmq-server`

**Tab 2**

View logs here

RUN `celery -A tasks worker --loglevel=info`

**Tab 3**

RUN `python task_runner.py`

Better yet we can simulate requests as from a browser through the flask app:

RUN `python flask_app.py`

Get to this [http://localhost:5000/celery_hack/100](http://localhost:5000/celery_hack/100) in the browser


**Tab 4**

AB Apache Benchmarking helps us analyze the requests. Reference [here](https://www.devside.net/wamp-server/load-testing-apache-with-ab-apache-bench)

RUN `ab -r -n 100 -c 10 -k -H "Accept-Encoding: gzip, deflate" http://127.0.0.1:5000/celery_hack/1000`

##Testing

RUN `nosetests`

RUN `coverage run tests.py`

For both tests and coverage
RUN `nosetests --with-coverage`

---
Copyright AD-2016
###### [Stanley Ndagi](http://techkenyans.org/jamii/stanmd) c/o [Andela](http://andela.com)
