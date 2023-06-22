import click
import pandas as pd
import yaml
from sklearn.model_selection import train_test_split


def square_foots_to_meters(foots: int) -> int:
    return round(foots * 0.092903)


def usd_to_rub(usd: int) -> int:
    return int(usd * 82 / 1000)


@click.command()
@click.option('--in_data', default='../data/raw/kaggle/train.csv')
@click.option('--out_data', default='../data/raw/kaggle/train.csv')
@click.option('--config', default='../params/preprocess_kaggle.yml')
def preprocess_data(in_data, out_data, config):
    with open(config) as f:
        config = yaml.safe_load(f)
        print(config)
    df = pd.read_csv(in_data)
    new_df = df[['GrLivArea', 'SalePrice']]
    print(new_df.head())
    new_df.loc[:, 'GrLivArea'] = new_df['GrLivArea'].apply(square_foots_to_meters)
    new_df.loc[:, 'SalePrice'] = new_df['SalePrice'].apply(usd_to_rub)
    new_df.to_csv(out_data)
    name_mapper = {
        'GrLivArea': 'total_meters',
        'SalePrice': 'price_per_month'
    }
    new_df = new_df.rename(columns=name_mapper)
    print(new_df.head())
    train_df, test_df = train_test_split(new_df, test_size=0.2)
    train_df.to_csv(config['train_out'])
    test_df.to_csv(config['test_out'])

if __name__ == '__main__':
    preprocess_data()
