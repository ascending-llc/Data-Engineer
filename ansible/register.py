import yaml
import boto3
import json
import os

client = boto3.client('lambda')

cwd = os.getcwd()

with open("./UserInfo.yaml", 'r') as stream:
    try:
        a = yaml.full_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for i in a['users']:
	response = client.invoke(
		FunctionName='cloudera-lambda-CreateIamUser-1APZ0OUSDRPIS',
		Payload=json.dumps(i, indent=2).encode('utf-8')
	)


os.system('ansible-playbook CreateUser.yaml -e @'+cwd+'/UserInfo.yaml')