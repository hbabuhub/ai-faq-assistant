import boto3
import json

def get_claude_answer(question):
    # Create a Bedrock client
    client = boto3.client('bedrock-runtime', region_name='us-east-1')

    # Correct model ID for Claude 3.5 Sonnet
    model_id = "Enter the model ID"

    # Prepare the messages with the question
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": question}
            ]
        }
    ]

    # Create the input payload
    input_payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": messages
    }

    # Call the model
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(input_payload),
        contentType="application/json",
        accept="application/json"
    )

    # Decode the response body
    response_body = response['body'].read().decode('utf-8')

    # Extract the response text from the content list
    response_json = json.loads(response_body)
    answer = response_json['content'][0]['text']

    return answer

