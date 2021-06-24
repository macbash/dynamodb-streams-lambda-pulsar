# dynamodb-streams-lambda-pulsar
Dynamodb Streams to Pulsar Topic Producer using Lambda

## WorkFlow
```Dynamodb Streams => Lambda Function ( Producer ) => Apache Pulsar Cluster```

## IAM Pre-Reqs
```
1.Dynamodb Stream Read Access
2.S3 Bucket
3.EC2 - ENI Creation for lambda
```

## Deployment Bundle
```File: Deployment.zip ( upload to s3 and deploy in lambda )```
