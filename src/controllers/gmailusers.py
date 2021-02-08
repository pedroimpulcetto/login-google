from flask_restplus import Resource

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from src.server.instance import server

app, api = server.app, server.api

cred = credentials.Certificate(".env/key.json")
firebase_admin.initialize_app(cred)

# https://firebase.google.com/docs/firestore/quickstart?hl=pt-br

@api.route('/gmailusers')
class GmailusersList(Resource):
    def get(self, ):
        gmail_users_db = firestore.gmailusers()
        
        return gmail_users_db

    def post(self, ):
        response = api.payload
        return response, 200


"""
    TODO : Falta criar os seguintes procedimento:
        - Logar os usuários através da conta do Google GMAIL, armazenar o login na collection gmailusers (table) se não
        estiver cadastrado. Só após usuário estiver cadastrado e logado com conta GMAIL, poderá consultar contatos.
        - GET para consultar os contatos do gmail do usuário logado, consumir API Google Person (https://developers.google.com/people)
            A lista deve retornar os contatos que tem emails, agrupados pelo domínio do email, ordem crescente
"""
