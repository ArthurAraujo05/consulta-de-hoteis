from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    
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

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Erro interno do servidor'}, 500
            return {'message': 'Hotel deletado'}
        return{'message': 'Hotel nao encontrado.'}, 404