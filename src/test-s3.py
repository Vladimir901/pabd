#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import boto3
from dotenv import dotenv_values, load_dotenv

bucket_name = "vladimir-s3-bucket"
load_dotenv("../.env")
# aws_access_key_id = os.getenv("aws_access_key_id")
# aws_secret_access_key = os.getenv("aws_secret_access_key")

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    # aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key
)

# # Создать новый бакет
# s3.create_bucket(Bucket='bucket-name')

# Загрузить объекты в бакет

## Из строки
# s3.put_object(Bucket='bucket-name', Key='object_name', Body='TEST', StorageClass='COLD')
#
# ## Из файла
# s3.upload_file('../data/raw/cian/cian_parsing_result_rent_long.csv', bucket_name, 'cian_parsing_result_rent_long.csv')
# s3.upload_file('this_script.py', 'bucket-name', 'script/py_script.py')

# # # Получить список объектов в бакете
# for key in s3.list_objects(Bucket=bucket_name)['Contents']:
#     print(key['Key'])

# # Удалить несколько объектов
# forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
# response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': forDeletion})
#
# # Получить объект
# get_object_response = s3.get_object(Bucket='bucket-name',Key='py_script.py')
# print(get_object_response['Body'].read())