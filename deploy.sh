#!/bin/bash

sam package --s3-bucket ascending-devops --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --region us-east-1 --capabilities CAPABILITY_IAM --stack-name cloudera-lambda