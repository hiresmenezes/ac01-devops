import json

def lambda_handler(event, context):   
    response = {}
    response["statusCode"]=301
    response["headers"]={

        'Location':'https://chat-mesa-de-bar.s3.amazonaws.com/pag_6-encontrar-galera.html'
    }
    data = {}
    response["body"]=json.dumps(data)
    return response
