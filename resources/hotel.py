from flask_restful import Resource, reqparse

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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Nenhum hotel encontrado.'} , 404
    
    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('cidade')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')

        dados = argumentos.parse_args()

        novo_hotel = {
                'hotel_id': hotel_id,
                'nome': dados['nome'],
                'estrelas': dados['estrelas'],
                'cidade': dados['cidade'],
                'diaria': dados['diaria']
            }

        hoteis.append(novo_hotel)
        return novo_hotel, 200
        


    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass