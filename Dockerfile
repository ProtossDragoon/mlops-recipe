FROM python:3.8.16-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 파일을 작업 디렉토리에 복사
COPY requirements.txt /app/

# requirements.txt 에 명시된 패키지 설치
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 모델을 작업 디렉토리에 복사
COPY mlp-model/ /app/mlp-model/

# 모든 파이썬 소스 코드를 작업 디렉토리에 복사
COPY *.py /app/

EXPOSE 8080

ENTRYPOINT [ "python3", "app.py" ]
