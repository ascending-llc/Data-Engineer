import boto3
import secrets
import string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

	group_dict = { 'students': 'DataEngineerStudents', 'instructors': 'DataEngineerInstructors'}

	response = client.add_user_to_group(
		GroupName=group_dict[event['group']],
		UserName=event['username']
		)

	alphabet = string.ascii_letters + string.digits
	password = ''.join(secrets.choice(alphabet) for i in range(10))

	response = client.create_login_profile(
    	UserName=event['username'],
    	Password=password,
    	PasswordResetRequired=True
	)

	client_ssm = boto3.client('ssm')
	response_ssm = client_ssm.get_parameters(Names=['sendgrid-api'])


	message = Mail('no-reply@ascendingdc.com',
		to_emails=event['email'],
		subject='AWS Console Credentials',
		html_content='https://595312265488.signin.aws.amazon.com/console' + '<br>' + 'Your username is ' + event['username'] + '<br>' + 'Your temporary password is ' + password + '<br>' + 'Connect to jumpbox server: ssh ' + event['username'] + '@54.86.193.122')

	try:
		sg = SendGridAPIClient(response_ssm['Parameters'][0]['Value'])
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e.message)