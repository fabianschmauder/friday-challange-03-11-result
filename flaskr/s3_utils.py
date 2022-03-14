import boto3

client = boto3.client("s3")

def list_objects(bucketname):
    response = client.list_objects(Bucket = bucketname)
    return response["Contents"]


def count_words_in_object(bucketname, key):
    response = client.get_object(Bucket = bucketname, Key = key)
    object_content =  response["Body"].read()
    split = object_content.split()
    return len(split)