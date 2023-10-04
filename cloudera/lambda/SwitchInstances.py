import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag-key',
            'Values': [
                'Cloudera',
            ]
        },
    ]
)

res = response['Reservations']

instances = []
for i in res:
	instances.append(i['Instances'][0]['InstanceId'])

def switch_instances(event,context):
    if event['status'] == 'on':
        response = client.start_instances(InstanceIds=instances)
    elif event['status'] == 'off':
        response = client.stop_instances(InstanceIds=instances)