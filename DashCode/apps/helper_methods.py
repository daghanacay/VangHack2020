import boto3

s3 = boto3.client('s3')

def get_portfolio_returns():
    # First try s3
    pass