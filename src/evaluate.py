from datetime import datetime

import pandas as pd
import yaml
from joblib import load
from sklearn.metrics import mean_squared_error

config_path = '../params/evaluate.yml'


def make_test_report(X, Y, config, model):
    score = model.score(X, Y)
    y_pred = model.predict(X)
    mse = mean_squared_error(Y, y_pred, squared=False)
    report = [
        f'Training datetime: {datetime.now()}\n',
        f'Training data len: {len(X)}\n',
        f'R^2: {score:.4f}\n',
        f'MSE: {mse:.4f} *1000 RUB \n',
    ]
    with open(config['report_path'], 'w', encoding='utf8') as f:
        f.writelines(report)


if __name__ == '__main__':
    with open(config_path) as f:
        config = yaml.safe_load(f)

    model = load(config['model_path'])
    test_df = pd.read_csv(config['test_df'])
    X = test_df['total_meters'].to_numpy().reshape(-1, 1)
    y_true = test_df['price_per_month']
    make_test_report(X, y_true, config, model)