#!/usr/bin/env python3

# 내장
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# 서드파티
import click
import requests

# 프로젝트
from myopslib import predict


@click.command("inference", help="머신러닝 모델을 사용하여 추론을 수행")
@click.option("--cylinders", required=True, type=int)
@click.option("--displacement", required=True, type=float)
@click.option("--horsepower", required=True, type=int)
@click.option("--weight", required=True, type=int)
@click.option("--acceleration", required=True, type=float)
@click.option("--modelyear", required=True, type=int, help="01(1900)~99(1999) 두자리를 입력")
@click.option("--country", required=True, type=click.Choice(["USA", "Japan", "Europe"]))
@click.option("--host", help="url을 입력하면 http 요청을 통해 실행")
def inference(
    cylinders: int,
    displacement: float,
    horsepower: int,
    weight: int,
    acceleration: float,
    modelyear: int,
    country: str,
    host: str,
):
    x = {
        "Cylinders": cylinders,
        "Displacement": displacement,
        "Horsepower": horsepower,
        "Weight": weight,
        "Acceleration": acceleration,
        "ModelYear": modelyear,
        "Country": country,
    }
    click.echo(click.style(f"입력: \n{x}", bg="green", fg="white"))
    if host:
        click.echo(click.style(f"호스트: {host}", bg="green", fg="white"))
        result = requests.post(url=host, json=x, timeout=30)
        click.echo(click.style(f"응답: \n{result.text}", bg="red", fg="white"))
    else:
        result = predict(x)
        click.echo(click.style(f"추론: \n{result}", bg="red", fg="white"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    inference()
