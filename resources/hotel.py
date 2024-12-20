from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3

def normalize_path_params(cidade=None,
                          estrelas_min = 0,
                          estrelas_max = 5,
                          diaria_min = 0,
                          diaria_max = 1000,
                          limit = 50,
                          offset = 0, **dados):
                
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': limit,
            'offset': offset}
    return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'limit': limit,
            'offset': offset}

path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class Hoteis(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        

        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get('cidade'):
            consulta = "SELECT * FROM HOTEIS \
            WHERE (estrelas > ? and estrelas < ?) \
            and (diaria > ? and diaria < ?) \
            LIMIT ? OFFSET ?"
            tuple = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tuple)
        else:
            consulta = "SELECT * FROM HOTEIS \
            WHERE (estrelas > ? and estrelas < ?) \
            and (diaria > ? and diaria < ?) \
            and cidade ? LIMIT ? OFFSET ?"
            tuple = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tuple)

        hoteis = []
        for linha in resultado:
            hoteis.append({
            'hotel_id': linha[0],
            'name': linha[1],
            'cidade': linha[2],
            'estrelas': linha[3],
            'diaria': linha[4]
            })

        return {'hoteis': hoteis}
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type=str, required=True, help="Campo 'nome' obrigatorio!")
    argumentos.add_argument('estrelas', type=float, required=True, help="Campo 'estrelas' obrigatorio!")
    argumentos.add_argument('cidade')
    argumentos.add_argument('diaria')
 
            
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Nenhum hotel encontrado.'} , 404
    
    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Erro interno do servidor'}, 500
        return hotel.json()

    @jwt_required()    
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Erro interno do servidor'}, 500
        return hotel.json(), 201
    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Erro interno do servidor'}, 500
            return {'message': 'Hotel deletado'}
        return{'message': 'Hotel nao encontrado.'}, 404