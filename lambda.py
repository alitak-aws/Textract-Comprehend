import json
import boto3

print('Loading function')

s3 = boto3.client('s3')
textract = boto3.client('textract')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    document = event['Records'][0]['s3']['object']['key']
    
    print(document)

    #process using S3 object
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': document
            }
        })

    #Get the text blocks
    blocks=response['Blocks']
    
    return {
        'statusCode': 200,
        'body': json.dumps(blocks)
    }
