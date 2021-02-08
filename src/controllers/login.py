from flask import request
from flask_restplus import Resource

from src.server.instance import server
from src.models.login import LoginModel

api = server.api

@api.route('/login', methods=['POST'])
class Login(Resource):
    def post(self, ):
        data = request.json

        status_code = 200
        response = {'message': 'Login accepted'}

        login_model = LoginModel()

        try:
            login_model.make_login(data)
        except Exception as ex:
            status_code = 500
            response = ex
        
        return response, status_code