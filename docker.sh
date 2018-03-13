#!/usr/bin/env bash

find . -name '*.pyc' -delete

docker build -t monit-app .
docker run -it monit-app
