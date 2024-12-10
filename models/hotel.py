class HotelModel:
    def __init__(self, hotel_id, name, cidade, estrelas, diaria):
        self.hotel_id = hotel_id
        self.name = name
        self.cidade = cidade
        self.estrelas = estrelas
        self.diaria = diaria

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'cidade': self.cidade,
            'estrelas': self.estrelas,
            'diaria': self.diaria
        }
