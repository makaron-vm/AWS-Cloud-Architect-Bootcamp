import boto3
import sys


def main():
    list3bucket()

def list3bucket():
    client = boto3.client('s3')

    list = client.list_buckets()

    print(list)


if __name__ == '__main__':
    main()