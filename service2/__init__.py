
import logging
import azure.functions as func
import random
import string

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letters = string.ascii_lowercase
    letterstring = ''.join(random.choice(letters) for i in range(5))
    return letterstring