#!/usr/bin/env bash

find . -name '*.pyc' -delete

docker build -t monit-app .
docker run -p5000:5000 -it monit-app
