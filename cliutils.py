#!/usr/bin/env python3

# 내장
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# 서드파티
import click

# 프로젝트
import myopslib


@click.group()
@click.version_option("1.0")
def cli():
    pass


@cli.command("retrain", help="머신러닝 모델 추가학습")
def retrain():
    click.echo(click.style("모델 추가학습", bg="green", fg="white"))
    mae = myopslib.retrain()
    click.echo(click.style(f"추가학습 MAE: {mae}", bg="blue", fg="white"))


# 필요하다면 추가로 다른 명령어를 추가할 수 있습니다.

if __name__ == "__main__":
    cli()
