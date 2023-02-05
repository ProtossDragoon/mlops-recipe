#!/usr/bin/env bash

docker build --tag=mlops-recipe .
docker run -p 127.0.0.1:8080:8080 mlops-recipe
