all: install lint test format

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint --disable=R,C,W1203,E1101 *.py

test:
	python3 -m unittest discover -s . -p "*_test.py" -v

format:
	black *.py
