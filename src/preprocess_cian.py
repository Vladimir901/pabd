import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

config_path = '../params/preprocess_cian.yml'


def read_cian_data(config):
    in_data = config['in_data']
    df = pd.read_csv(in_data, sep=';')
    return df[['total_meters', 'price_per_month']]


if __name__ == '__main__':
    with open(config_path, encoding='utf-8') as f:
        config = yaml.safe_load(f)
    df = read_cian_data(config)
    df['price_per_month'] = df['price_per_month']/1000
    df.drop(df[df.total_meters < 0].index)
    train_df, test_df = train_test_split(df, test_size=0.2)
    train_df.to_csv(config['train_out'])
    test_df.to_csv(config['test_out'])
