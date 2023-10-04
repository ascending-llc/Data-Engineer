import os
import psycopg2
import json

# Environment variables set in the Lambda function configuration
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

def lambda_handler(event, context):
    
    # Parse start_line and end_line from the event
    start_line = int(event['queryStringParameters']['start_line'])
    end_line = int(event['queryStringParameters']['end_line'])
    
    try:
        # Connect to your postgres instance
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=rds_host
        )

        cursor = conn.cursor()

        # Replace YOUR_TABLE with your actual table name
        sql_query = f"SELECT * FROM YOUR_TABLE LIMIT %s OFFSET %s;"
        cursor.execute(sql_query, (end_line - start_line, start_line))

        # Fetch the data
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, record)) for record in records]

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

    finally:
        cursor.close()
        conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

