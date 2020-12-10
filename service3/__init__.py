  
import logging
import azure.functions as func
import random

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    numbers = "123456789"
    nostring = ''.join(random.choice(numbers) for i in range(5))
    return nostring
