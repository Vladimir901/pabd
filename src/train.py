# train.py
from datetime import datetime
from pickle import dump

import click
import numpy as np
# from joblib import dump
import pandas as pd
import yaml
from sklearn.linear_model import LinearRegression
from joblib import dump

@click.command()
@click.option('--data_path', default='../data/processed/train.csv')
@click.option('--model_path', default='../models/model_1.joblib')
@click.option('--config', default='../params/train.yml')
def train(data_path, model_path, config):
    with open(config) as f:
        config = yaml.safe_load(f)

    train_df = pd.read_csv(data_path)
    X = train_df['GrLivArea'].to_numpy().reshape(-1, 1)
    Y = train_df['SalePrice']

    model = LinearRegression().fit(X, Y)
    make_report(X, Y, config, model)
    dump(model, model_path)


def make_report(X, Y, config, model):
    score = model.score(X, Y)
    coef, intercept = model.coef_[0], model.intercept_
    report = [
        f'Training datetime: {datetime.now()}\n',
        f'Training data len: {len(X)}\n',
        f'R^2: {score:.4f}\n',
        f'Price: {int(coef)} * meters + {int(intercept)} rubles\n',
    ]
    for line in report:
        print(line)
    with open(config['report_path'], 'w', encoding='utf8') as f:
        f.writelines(report)


if __name__ == "__main__":
    print("Start training model")
    train()
    print("Done")
