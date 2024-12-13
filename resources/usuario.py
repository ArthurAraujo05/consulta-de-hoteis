from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from secrets import compare_digest
from blacklist import BLACKLIST



atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="O campo 'login' nao pode ser deixado em branco")
atributos.add_argument('senha', type=str, required=True, help="O campo 'senha' nao pode ser deixado em branco")


class User(Resource):
            
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'Nenhum usuario encontrado.'} , 404
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'Erro interno do servidor'}, 500
            return {'message': 'Usuario deletado'}
        return{'message': 'Usuario nao encontrado.'}, 404
    
class UserResgister(Resource):
    
    def post(self):

        dados = atributos.parse_args()
        
        if UserModel.find_by_login(dados['login']):
            return {"message": "O login '{}' ja existe.".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()
        return {"message": 'Usuario criado com sucesso!'}, 201
    
class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and compare_digest(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'messagem': 'usuario ou senha esta incorreto'}, 401
    
class UserLogout(Resource):
    def post(self):
        jwt_id = get_jwt(['jti'])
        BLACKLIST.add(jwt_id)
        return {'message': 'Logout feito com sucesso'}
