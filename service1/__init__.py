import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letterstring = requests.get('https://appserverless.azurewebsites.net/api/service2?code=aIjyCfy/YyF127KlciSzC7NrwNfqn1waGSZbZ0kQZnmlYjznQIUO5g==').text
    nostring = requests.get('https://appserverless.azurewebsites.net/api/service3?code=OYvFXuUAzEaZ85d5nJSwaEWq1Dcv6XCvR6VhNmdXwyArxVLdUT4MwA==').text
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]

    endpoint = "https://ryan.documents.azure.com:443/"
    key = "tmWgihjw68kOrkMSzMCdU8JOaj1ofw9mmxujRnBLedHAMMHFwery3brqMRlrV2HDOj6p1sBLWx5XjwB1GUAiVA=="
    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    database=client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)
    return username
