import json
import boto3
from datetime import datetime


dynamodb = boto3.resource('dynamodb')
tableMessages = dynamodb.Table('ChatMesaDeBar')


def lambda_handler(event, context):
    data_hora = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    remetente = str(event['from'])
    destinatario = str(event['to'])
    mensagem = str(event['msg'])

    try:
        tableMessages.put_item(
            Item = {
                'remetente': remetente,
                'data_hora': data_hora, 
                'destinatario': destinatario,
                'mensagem': mensagem
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Mensagem de '
                                + remetente
                                + ' para '
                                + destinatario
                                + ' inserida no Banco de Dados')
        }
        
    except:
        print('Erro: lambda function terminada com sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
