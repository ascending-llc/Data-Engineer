import boto3

client = boto3.client('iam')

def create_aws_user(event,context):
	response = client.create_user(
		UserName=event['username'],
		Tags=[
			{
				'Key': 'group',
				'Value': event['group']
			}
		]
	)

	group_dict = { 'student': 'DataEngineerStudents', 'instructor': 'DataEngineerInstructors'}

	response = client.add_user_to_group(
		GroupName=group_dict[event['group']],
		UserName=event['username']
		)

	response = client.create_login_profile(
    	UserName=event['username'],
    	Password='1234abcd',
    	PasswordResetRequired=True
	)