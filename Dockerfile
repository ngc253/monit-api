FROM centos:7

MAINTAINER Sridhar Vemula

RUN curl https://bootstrap.pypa.io/get-pip.py --output /tmp/pip.py && python /tmp/pip.py && rm -rf /tmp/pip.py && python -m pip install --upgrade pip setuptools wheel flask

ADD . /data/env/monit/

RUN cd /data/env/monit && rm -rf migrations && pip install -r requirements.txt

EXPOSE 5000

ENV APP_SETTINGS 'src.config.DockerConfig'

CMD cd /data/env/monit && python manage.py db init &&  python manage.py db migrate && python manage.py db upgrade && python manage.py runserver -h 0.0.0.0


