#!/usr/bin/env bash

docker build --tag=mlops-recipe:v1 .
docker run --rm -p 127.0.0.1:8080:8080 mlops-recipe:v1
