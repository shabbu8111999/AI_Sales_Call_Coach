import boto3

s3 = boto3.client("s3")

BUCKET_NAME = "sales-call-audio-bucket-shabareesh"
FILE_PATH = "data/Conversation.mp3"

s3.upload_file(FILE_PATH, BUCKET_NAME, "Conversation.mp3")

print("Audio uploaded to S3 successfully")