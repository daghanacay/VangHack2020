# import boto3
#
# def get_portfolio_returns():
#     client = boto3.client('s3', aws_access_key_id=aws_id,
#                           aws_secret_access_key=aws_secret)
#     csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
#     body = csv_obj['Body']
#     csv_string = body.read().decode('utf-8')
#
#     df = pd.read_csv(StringIO(csv_string))