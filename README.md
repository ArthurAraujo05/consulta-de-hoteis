# Hotel API

Esta é uma API simples de gerenciamento de hotéis criada com o framework **Flask** e a extensão **Flask-RESTful**. A API permite realizar operações CRUD (Create, Read, Update, Delete) em uma lista de hotéis.

## Endpoints

### 1. **GET /hoteis**
Retorna uma lista de todos os hotéis.

**Exemplo de resposta:**

```json
{
  "hoteis": [
    {
      "hotel_id": "victoria",
      "name": "Victoria Resort",
      "cidade": "Campinas",
      "estrelas": 5.0,
      "diaria": 490.50
    },
    {
      "hotel_id": "lisa",
      "name": "Lisa Hotel",
      "cidade": "Vinhedo",
      "estrelas": 4.2,
      "diaria": 320.50
    },
    {
      "hotel_id": "plazza",
      "name": "Plazza Resort",
      "cidade": "Hortolândia",
      "estrelas": 2.0,
      "diaria": 180.50
    }
  ]
}
