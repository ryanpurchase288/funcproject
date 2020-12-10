import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letterstring = requests.get('https://appserveless.azurewebsites.net/api/service2?code=1sfWuUECuyjhfR5LyHuNHNTA3aL7a2MgG9EnBMVMnXdDvALzUTWWMA==').text
    nostring = requests.get('https://appserveless.azurewebsites.net/api/service3?code=SNmyvhsMyHksv1sj60Drqqa2i819tm2aulUBL4YJCpemkyB0ZQOeSA==').text
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]

    endpoint = "https://ryan.documents.azure.com:443/"
    key = "vHfiVCGlnLpYIK03FcB6uiJAHLnjoOhQFCjHRHwr2sdJ8yeTRcRNT5tty3zMgZCQwY0rgeIITF0sx2TRycbkAA=="
    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    database=client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
        offer_throughput=400
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)
    return username
