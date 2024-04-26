# Address retrieval application

## How to start

Run from project root

```shell
docker compose up --build
```

Port is set through `APP_PORT` variable in config.py. Default is 8000

## Examples

**GET Requst URL: http://localhost:8000/**
Response body:
```json
{
    "status": "running",
    "cores": 8
}
```

**POST Request URL: http://localhost:8000/process/batch**
Request body:
```json
{
    "text": ["Вчера на улице Невельского в ближайшем Ростиксе продавали курочку с рисом. Тимур встретил свою маму в метро и зашел купить себе ужин. После они медленно и неторопливо отправились домой.", "В Подольске совсем грустно стало без вас. Вася, который на Володарской улице жил, без вас вовсе одичал"]
}
```

Response body:
```json
{
    "result": [
        [
            "улица Невельского"
        ],
        [
            "город Подольск",
            "город Подольск, улица Володарская"
        ]
    ]
}
```

**POST Request URL: http://localhost:8000/process/single**
Request body:
```json
{
    "text": "Вчера на улице Невельского в ближайшем Ростиксе продавали курочку с рисом. Тимур встретил свою маму в метро и зашел купить себе ужин. После они медленно и неторопливо отправились домой."
}
```

Response body:
```json
{
    "result": [
        "улица Невельского"
    ]
}
```
