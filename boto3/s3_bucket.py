import boto3
import sys


def main():
    creats3bucket(name)

def creats3bucket(name):
    client = boto3.client('s3')

    create = client.create_bucket(
        ACL='private',
        Bucket=name,
        CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },
    )

    print(create)


name = sys.argv[1]

if __name__ == '__main__':
    main()