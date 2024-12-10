from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
        {
        'hotel_id':'victoria',
        'name':'Victoria Resort',
        'cidade': 'Campinas',
        'estrelas': 5.0,
        'diaria': 490.50
        },
        {
        'hotel_id':'lisa',
        'name':'Lisa Hotel',
        'cidade' :'Vinhedo',
        'estrelas': 4.2,
        'diaria': 320.50
        },
        {
        'hotel_id':'plazza',
        'name':'Plazza Resort',
        'cidade': 'hortolandia',
        'estrelas': 2.0,
        'diaria': 180.50
        },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name')
    argumentos.add_argument('cidade')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None   
            
    def get(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Nenhum hotel encontrado.'} , 404
    
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201
        
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deletado'}