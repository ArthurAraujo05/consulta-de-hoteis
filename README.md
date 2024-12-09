```markdown
# Hotel API

Esta é uma API simples de gerenciamento de hotéis criada com o framework **Flask** e a extensão **Flask-RESTful**. A API permite realizar operações CRUD (Create, Read, Update, Delete) em uma lista de hotéis.

## Endpoints

### **1. GET /hoteis**
Retorna uma lista de todos os hotéis.

#### Exemplo de Requisição:

```http
GET /hoteis HTTP/1.1
Host: localhost:5000
```

#### Exemplo de Resposta:

```json
[
  {
    "hotel_id": "victoria",
    "name": "Victoria Resort",
    "cidade": "Campinas",
    "estrelas": 5.0,
    "diaria": 490.50
  },
  ...
]
```

### **2. GET /hoteis/{hotel_id}**
Retorna informações sobre um hotel específico.

#### Exemplo de Requisição:

```http
GET /hoteis/victoria HTTP/1.1
Host: localhost:5000
```

#### Exemplo de Resposta:

```json
{
  "hotel_id": "victoria",
  "name": "Victoria Resort",
  "cidade": "Campinas",
  "estrelas": 5.0,
  "diaria": 490.50
}
```

### **3. POST /hoteis/novo_hotel**
Adiciona um novo hotel.

#### Exemplo de Requisição:

```http
POST /hoteis/novo_hotel HTTP/1.1
Host: localhost:5000
Content-Type: application/json
```

```json
{
  "nome": "Novo Hotel",
  "cidade": "São Paulo",
  "estrelas": 4.5,
  "diaria": 350.00
}
```

#### Exemplo de Resposta:

```json
{
  "hotel_id": "novo_hotel",
  "name": "Novo Hotel",
  "cidade": "São Paulo",
  "estrelas": 4.5,
  "diaria": 350.00
}
```

### **4. PUT /hoteis/{hotel_id}**
Atualiza as informações de um hotel.

#### Exemplo de Requisição:

```http
PUT /hoteis/victoria HTTP/1.1
Host: localhost:5000
Content-Type: application/json
```

```json
{
  "nome": "Hotel Atualizado",
  "cidade": "Campinas",
  "estrelas": 4.8,
  "diaria": 400.00
}
```

#### Exemplo de Resposta:

```json
{
  "hotel_id": "victoria",
  "name": "Hotel Atualizado",
  "cidade": "Campinas",
  "estrelas": 4.8,
  "diaria": 400.00
}
```

### **5. DELETE /hoteis/{hotel_id}**
Deleta um hotel.

#### Exemplo de Requisição:

```http
DELETE /hoteis/victoria HTTP/1.1
Host: localhost:5000
```

#### Exemplo de Resposta:

```json
{
  "message": "Hotel deletado"
}
```

## Dependências

- `aniso8601==6.0.0`
- `Click==7.0`
- `Flask==1.0.2`
- `Flask-JWT-Extended==3.18.1`
- `Flask-RESTful==0.3.7`
- `Flask-SQLAlchemy==2.3.2`
- `itsdangerous==1.1.0`
- `Jinja2==2.10.1`
- `MarkupSafe==1.1.1`
- `PyJWT==1.7.1`
- `pytz==2019.1`
- `six==1.12.0`
- `SQLAlchemy==1.3.3`
- `Werkzeug==0.15.2`

## Instalação

### Passos para rodar a aplicação

1. **Clone o repositório** ou baixe os arquivos:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   Para criar o ambiente virtual:

   ```bash
   python -m venv venv
   ```

   Para ativar o ambiente (Windows):

   ```bash
   venv\Scripts\activate
   ```

   Para ativar o ambiente (Linux/macOS):

   ```bash
   source venv/bin/activate
   ```

3. Instale as dependências com:

   ```bash
   pip install -r requirements.txt
   ```

### Como rodar

Após instalar as dependências, execute o arquivo Python:

```bash
python app.py
```
``` 
